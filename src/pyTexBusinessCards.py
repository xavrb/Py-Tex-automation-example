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
tex_code = tex_code + """


% BUSINESS CARD template
% created by Karol Koziol (www.karol-koziol.net)
% for ShareLaTeX - online LaTeX editor (www.sharelatex.com)
% May 2013
%edited and powered by xavrb@github.com


\\documentclass[10pt]{article}
\\usepackage{fontspec}


\\setmainfont{Lato}
\\usepackage{graphicx}

\\usepackage{xcolor}
\\usepackage{tikz}
\usepackage{ifthen}

\\usepackage{geometry}
\\geometry{total={210mm,297mm},hmargin=10mm,vmargin=2mm}

\\pagestyle{empty}

%\\renewcommand\\familydefault{\\sfdefault}
\\usepackage{tgadventor}



%%% BUSINESS CARD SIZE
\\newlength{\\cardw}
\\newlength{\\cardh}

\\ifthenelse{\equal{\cardSize}{iso7810}}{
    %% ISO 7810 size: 85.60mm x 53.98mm
    \\setlength{\\cardw}{85.60mm}
    \\setlength{\\cardh}{53.98mm}
}{
\\ifthenelse{\equal{\cardSize}{european}}{
    %% European size: 85mm x 55mm
    \\setlength{\\cardw}{85mm}
    \\setlength{\\cardh}{55mm}
}{
\\ifthenelse{\equal{\cardSize}{us}}{
    %% US size: 3.5 in x 2 in
    \\setlength{\\cardw}{3.5in}
    \\setlength{\\cardh}{2in}
}{
     }
}
}



\\begin{document}
\\foreach \\z in {0,...,\\numberPages} {\\begin{tikzpicture}
% grid
\\foreach \\i in {0,...,5} \\draw[very thin, gray,solid] (0,\\i*\\cardh) -- (2*\\cardw,\\i*\\cardh);
\\foreach \\j in {0,...,2} \\draw[very thin, gray,solid] (\\j*\\cardw,0) -- (\\j*\\cardw,5*\\cardh);
% card content
\\foreach \\i in {0,1} \\foreach \\j in {0,...,4} {
   \\node at (\\i*\\cardw+0.2\\cardw,\\j*\\cardh+0.5\\cardh) {\\includegraphics[width=0.2\\cardw]{logo}};
% center text
   \\node[black!25!gray] at (\\i*\\cardw+0.65\\cardw,\\j*\\cardh+0.75\\cardh) {\\Large{\\Name}\\Huge{\\Lname}};
   \\node at (\\i*\\cardw+0.65\\cardw,\\j*\\cardh+0.63\\cardh) {\\DegreeDesc};
      \\node at (\\i*\\cardw+0.65\\cardw,\\j*\\cardh+0.53\\cardh) {\\Address};

   \\node at (\\i*\\cardw+0.65\\cardw,\\j*\\cardh+0.35\\cardh) {\\Cellphone};
   \\node at (\\i*\\cardw+0.65\\cardw,\\j*\\cardh+0.25\\cardh) {\\Landline};
   \\node at (\\i*\\cardw+0.65\\cardw,\\j*\\cardh+0.1\\cardh) {\\large{\\EmailUsername} @\\EmailDomain};
};
\\end{tikzpicture}
\\newpage}
\\end{document}

"""



build_d = "{}results/".format(project)
out_file = "{}businessCards{}-{}".format(build_d, options[0][1],options[1][1]) #naming file after users name

if not os.path.exists(build_d):  # create the build directory if not existing
    os.makedirs(build_d)

with open(out_file+".tex", "w") as f:  # saves tex_code to output file
    f.write(tex_code)
print "TeX generated!"
os.system("xelatex -output-directory {} {}".format(os.path.realpath(build_d), os.path.realpath(out_file)))#compiling generated tex
os.system("xdg-open {}.pdf ".format(os.path.realpath(out_file)))
print "\n\n===============\nPDF generated, options used: \n" + str(options)
print "Cleaning aux files"
os.system("rm -rf {}.aux {}.log".format(os.path.realpath(out_file),os.path.realpath(out_file))) #cleaning build dir
