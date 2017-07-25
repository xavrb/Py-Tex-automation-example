# pyTexBusinessCards

Getting your business card nice and clean with a single line.


## Getting started
These instructions will get you a copy of the project up and running on your local machine for development, testing and creation purposes. 

### Prerequisites

What things you need to install the software and how to install them, I use Fedora but commands should not differ that much on debian based systems (please change accordingly).

I assume you have a working Python and Tex environments working.

```shell
# dnf install texlive-fontspec

# dnf install texlive-labels

```

#### Lato Font

For the business cards I use Lato, an elegant and nice font you can find at Google Fonts, download it and install on your system (Regular style will do the trick here)

```
https://fonts.google.com/specimen/Lato
```


 
## Clone    
 
```shell
git clone https://github.com/xavrb/pyTexBusinessCards
cd pyTexBusinessCards && cd src

```

## Configure
On /src/config-tex2bc.bcf you can configure your name, title, address, mail and phone. As well as the number of cards you need.

``` 
%Name: John
%Lname: Does
%DegreeDesc: Engineer
%Address: Westminster, London SW1A 0AA, UK
%EmailUsername: johndoe
%EmailDomain: testmail.ch
%Cellphone: 55233256565
%Landline: 56465454
%numberCards: 1500 <-- here you set the number of cards you need
%template: default <-- working on different templates 
 
```

### Start

```shell
python pyTexBusinessCards.py
```


## Preview

Code generated business cards will look like this:
![businesscard](https://github.com/xavrb/pyTexBusinessCards/blob/master/src/example/image_2017-07-25_00-09-04.png)

