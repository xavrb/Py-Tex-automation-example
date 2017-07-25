import re # import regular expressions module
import os #to handle files directly in the system


project = "./" # specify the project folder
in_file = "{}config-tex2bc.bcf".format(project) # path to the config file

with open(in_file) as f:    # loads the file
    content = f.read()
    keys = re.findall(r"%(.+):", content)   # find the keys using RegEx
    values = re. findall(r":\s*([\w\W]+?)\s*(?:%|$)", content) # find the values using RegEx

options = zip(keys, values) # combining keys and values in one nested list


tex_code = "" # send keys & values to a latex command as constants
for key, value in options:
    tex_code = tex_code + "\\newcommand{{\\{}}}{{{}}}\n".format(key, value)
print tex_code
tex_code = tex_code + """

\\documentclass{article} % din a4, 11 pt, one-sided,
\\usepackage[newdimens]{labels}
\\usepackage{fontspec}


\\setmainfont{Lato}
\\LabelCols=2%
\\LabelRows=4%
\\LeftPageMargin=5.0mm%
\\RightPageMargin=8.0mm%
\\TopPageMargin=5.0mm%
\\BottomPageMargin=5.0mm%
\\InterLabelColumn=0mm%
\\InterLabelRow=5.0mm%
\\LeftLabelBorder=5mm%
\\RightLabelBorder=5mm%
\\TopLabelBorder=2.0mm%
\\BottomLabelBorder=2mm%
\\numberoflabels=\\numberCards%
\\LabelGridtrue%  <-- or \LabelGridfalse
\\newcommand{\phonei}{\Cellphone}
\\newcommand{\phoneii}{\Landline}
\\newcommand{\emaili}{\EmailUsername}
%
\\begin{document}
\\addresslabel[\\fboxsep=5mm]{%
    {%
    \\raggedright%
    {\\Large \\Name}\\\\[1ex] %NAME
    {\\Huge \\textbf{\\Lname}}\\\\[1ex] %NAME
    \\textit{\\DegreeDesc}\\\\ %Degree
    \\vspace{4ex}
    \\Address\\\\
    Contact:\\\\
    \\hfill{\\small\\textit{\\phonei}}\\\\%
    \\hfill{\\small\\textit{\\phoneii}}\\\\[2ex]%
    \\hfill{\\small\\sffamily\\Large{\\textbf{\\emaili}}@\\EmailDomain}%
    }%
}
%This is a simple test using python and latex (texlive-labels).
%coded by xavrb
\\end{document}
"""



build_d = "{}results/".format(project)
out_file = "{}businessCards{}-{}".format(build_d, options[0][1],options[1][1]) #naming file after users name

if not os.path.exists(build_d):  # create the build directory if not existing
    os.makedirs(build_d)

with open(out_file+".tex", "w") as f:  # saves tex_code to output file
    f.write(tex_code)

os.system("xelatex -output-directory {} {}".format(os.path.realpath(build_d), os.path.realpath(out_file)))#compiling generated tex
os.system("xdg-open {}.pdf ".format(os.path.realpath(out_file)))
print "\n\n===============\nPDF generated, options used: \n" + str(options)
print "Cleaning aux files"
os.system("rm -rf {}.aux {}.log".format(os.path.realpath(out_file),os.path.realpath(out_file))) #cleaning build dir
