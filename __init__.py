#! python
''' See https://rivtDocs.net  for user manual

Introduction
============

rivt is an open source Python package that processes a new plain text markup
language - rivttext. rivttext was designed to write engineering documents that
can be shared as easily modified templates. rivt runs on any platform that
supports Python 3.8 or later and prioritizes simplicity, flexibility,
efficiency and universal access.

The rivt api wraps and extends the Github (gfm) and reStructuredText (reST)
markup languages defined at https://docutils.sourceforge.io/rst.html and xxx. 

A rivt file begins with the import statement:

*import rivt.rivtapi as rv*
 
which provides four API functions:
    
rv.R(rmS) - repository and report information (Repo)
rv.I(rmS) - static text, images, tables and math (Insert)
rv.V(rmS) - equations (Values)
rv.T(rmS) - Python functions and scripts (Tools)

A rivt document is made up of an arbitrary sequence of the three later string
methods following the initial method rv.R. Each method takes a single literal
(triple) string argument referred to as a rivt method string (rms) or rivt
string. When running in an IDE (e.g. VSCode), each method may be run
interactively using the standard cell decorator (# %%). The rv.writedoc() and
rv.reportdoc() functions generate documents and compilations in GitHub Markdown
(ghmd) and PDF formats. Interactive output to the terminal and VSCode
interative window is utf-8.

rivt works for both simple short documents and extensive reports. The rivt
folder structure shown below is designed to support both. A rivt project
includes public folders; *rivt-*report-label and *private* folders intended
for client and other confidential or proprietary files and information. 

Output files are written in two places, depending on the output type.
The Markdown output is written to a README.md file within the public *rivt-*
subfolder and may be read, searched and shared on version control platforms
like GitHub. Private information is not written to the README. The PDF output
is written to the doc folder in *private*.

Folder and file name prefixes that are fixed are shown in [ ] in the example
below. Folder labels may be combinations of specified prefixes and user labels.


Example Folder Structure (required prefixes shown in [ ])
=========================================================

[rivtproject]-Project-Label/
├── [rivt]-Report-Label/                    (public files)
    ├── .git
    ├── units.py                            (unit over-ride)
    ├── README.md                           (report toc)                                      
    └── [r0101]-Doc-Label1/
        ├── data/
            ├── data1.csv                   (input data)
            ├── data2.csv
            └── fig1.png
        ├── [r0101].py                      (document input)
        ├── README.md                       (output file)
        └── functions1.py                   (function file)
    ├── [r0102]-Doc-Label2/
        ├── data/
            ├── data1.csv
            ├── fig1.png
            └── fig2.png
        ├── [r0102].py
        ├── README.md
        └── functions2.py
    └── [r0201]-Doc- Labe3l/
       ├── data/
           ├── data1.csv
           ├── attachment.pdf
           └── fig1.png
       ├── [r0201].py
       ├── README.md
       └── functions3.py
└── [private]/                              (private files)
    ├── [rivt.ini]                          (config file)
    ├── project-info.txt
    ├── [temp]/                             (output files)
    ├── [report]/                           (output files)
        ├── r0101-Doc-Label1.pdf   
        ├── r0102-Doc-Label2.pdf
        ├── r0201-Doc-Label3.pdf
        └── Report-Label.pdf                (compiled PDF report)    
    ├── images/                             (optional data folders)
            ├── fig1.png
            └── fig2.png
    └── tables/
        ├── data1.csv
        └── data1.csv


The API is designed for sharing files in the *rivt-* folder. Files in this
folder include the core information in the document - the text, equations,
functions and tables. Files in the *private-* folder are typically not shared.
This two-part folder and file structure simplifies protection of confidential
content, while applying version control and sharing for the primary calculation
inputs.

Commands and Tags
=================

rivt syntax includes arbitrary unicode text and rivt commands and tags. Syntax
is interepreted by the particular rivt method. Commands read or write extrnal
files denoted by || at the beginning of a line. Command parameters are
separated by |. In the summary below single parameter options are separated by
semi-colons and list parameters are separated by commas. The first line of each
method is a section label followed by section parameters. Section labels may be
hidden by prepending with a double hyphen --.

Tags format a line or block of text and are generally denoted with _[tag] at
the end of a line. Block tags start the block of text with _[[tag]] and end
with _[[q]]. The "=" and ":=" tags used in the Value method are the
exceptions.


======= ===================================================================
 name             API Functions and commands (VSCode snippet prefix)
======= ===================================================================

Repo    rv.R("""label | page
(re)
                ||github (git)
                ||project (proj)
                ||append (app)

                """)

Insert  rv.I("""label | rgb; default
(in)
                ||image (img)
                ||text (tex)
                ||table (tab)

                """)

Values  rv.V("""label | sub; nosub 
(va)
                ||assign (ass)
                ||declare (dec)

                """)

Tools  rv.T("""label | rgb; default; noprint | space; nospace
(to)
                Python code

                """)

exclude rv.X("""any method

                A method changed to X is not evaluated and may be used for
                comments and debugging.

                """)

write   rv.writedoc('utf,pdf')
(wr)
=============================================================== ============
    command syntax and description (snippet)                         API 
=============================================================== ============

|| append | folder | file                                             R
    (ap)   pdf folder | .pdf; .txt  

|| github | folder | file                                             R
    (gi)   pdf folder | .pdf; .txt  
    
|| project | file                                 R
    (pr)   .txt; .tex; .html | plain; tags; latex

|| text | relative file path | text type                              I
    (te)   .txt; .tex; .html | plain; tags; code; math; latex

|| image  | relative file path | .50, ..                              I
    (im)   .png; .jpg |  page width fraction

|| table  | relative file path | 60,r;l;c | [:]                       I
    (ta)   .csv; xls  | max col width, locate | rows

|| declare | relative file path  | [:]                                V
    (de)    .csv; .xls  | rows

|| assign | relative file path  | [:]                                 V
    (as)    .csv; .xls  | rows

============================ ============================================
 tags                                   description 
============================ ============================================

Repo and Inserts:        
text _[b]                       bold 
text _[c]                       center
text _[i]                       italic
text _[r]                       right justify
text _[u]                       underline   
text _[l]                       LaTeX math
text _[s]                       sympy math
text _[e]                       equation label and autonumber
text _[f]                       figure caption and autonumber
text _[t]                       table title and autonumber
text _[#]                       footnote and autonumber
text _[d]                       footnote description 
_[page]                         new page
_[address, label]               url or internal reference

Inserts blocks:          
_[[b]]                          bold
_[[c]]                          center
_[[i]]                          italic
_[[p]]                          plain  
_[[l]]                          LaTeX
_[[h]]                          HTML 
_[[q]]                          quit block

Values formats: 
text _[l]                       LaTeX math
text _[s]                       sympy math
text _[e]                       equation label and autonumber
text _[f]                       figure caption and autonumber
text _[t]                       table title and autonumber
text _[#]                       footnote and autonumber
text _[d]                       footnote description 
a = n | unit, alt | descrip    declare = 
a := b + c | unit, alt | n,n   assign := 

The first line of a rivt file is always *import rivt.rivtapi as rv* followed by
the Repo method rv.R() which occurs once. rv.R is followed by any of the other
three methods in any number or order. rv.R() sets options for repository and
report output formats.

File format conventions follow the Python formatter pep8, and linter ruff.
Method names start in column one. All other lines must be indented 4 spaces to
facilitate section folding, bookmarks and legibility.

The first line of each rivt method defines the section title and section
parameters. 

============================================================================
rivt example
============================================================================

import rivt.rivtapi as rv

rv.R("""Introduction 

    The Repo method (short for repository or report) is the first method of a
    rivt doc and specifies repository settings and output formats.

    The setting line specifies the section label and colors. if any. If the
    label is preceded by two dashes "--", the the label becomes a reference and
    a new section is not started. If the color parameter (applies to PDF) is
    omitted then default black text and no background is used.

    The ||github command specifies a project README.md file in the public r00
    folder and the GitHub repository url where public project files are
    uploaded. It overwrites any existing README file. Files may also be
    uploaded directly using standard upload procedures.

    || github | file | upload repository

    The ||project command imports data from the private r00 folder. Its
    formatted output depends on the file type.

    || project | file | default

    The ||append command attaches PDF files to the end of the document.

    || append | file1 | title1
    || append | file2 | title2

    """)

rv.I("""Inserts method | rgb-fore,back; default

    The Insert method formats descriptive information that is static, as
    opposed to dynamic calculations and values.

    The ||text command inserts and formats text files. Text files may be plain
    text, latex, code, sympy math or include rivt tags.

    || text | file | text type
    plain; tags; code; math; latex

    Tags _[t] and _[f] format and autonumber tables and figures.

    table title  _[t]
    || table | data | file.csv | 60,r

    A figure caption _[f]
    || image | resource | f1.png | 50


    Insert two images side by side:

    The first figure caption  _[f]
    The second figure caption  _[f]
    || image | f2.png,f3.png | 45,35

    The tags [x]_ and [s]_ format LaTeX and sympy equations:

    \gamma = \frac{5}{x+y} + 3  _[x] 

    x = 32 + (y/2)  _[s]

    The url tag formats a url link.
    _[http://wwww.url, link label]

    The link tag formats an internal document link to a table, equation,
    section or paragraph title:
    _[lnk, existing label]

    """)

rv.V("""Values method | sub; nosub 

    The Values method assigns values to variables and evaluates equations. The
    sub;nosub setting specifies whether equations are also printed with
    substituted numerical values. 

    Example of assignment list _[t]
    f1 = 10.1 * LBF | N | a force
    d1 = 12.1 * IN | CM | a length

    An table tag provides a table title and number.  The equal tag declares a
    value. A sequence of declared values terminated with a blank line are
    formatted as a table.

    Example equation - Area of circle  _[e]
    a1 := 3.14(d1/2)^2 | IN^2, CM^2 | 2,2

    An equation tag provides an equation description and number. The
    colon-equal tag assigns a value and specifies the result units and printed
    output decimal places in the equation and results.

    || values | r0101 | s3
    
    The values command imports values from csv files written by rivt when
    processing assigned and declared values. The parameters specify the
    section number and doc number.

""")

rv.T("""Tools method | print;noprint | import folder | rgb fore,background
    
    # The Tools method processes Python code. The "print" parameter specifies #
    whether the code is echoed in the document. The "include" parameter #
    specifies whether the code values are subsequently available (i.e. #
    included in the document namespace).
    
    # Four libraries are imported by rivt as: 

    # pyplot (plt.)
    # numpy (np.)
    # pandas (pd.)
    # sympy (sy.)

    # Examples of Python code:

    # Define a function -S
    def f1(x,y): z = x + y
        print(z)
        return
    
    # Read and write files -    
    with open('file.csv', 'r') as f: 
        input = f.readlines()
    
    var = range(10)
    with open('fileout.csv', 'w') as f: 
        f.write(var)
        
    """)

rv.X("""any text

    Replacing the method letter with X skips evaluation of that string. Its
    uses include review comments, checking and editing.

    """) 

============== =========================================================
Keystroke                   VSCode rivt shortcuts and extensions
============== =========================================================

alt+q                rewrap paragraph with hard line feeds (80 default)
alt+.                select correct spelling under cursor
alt+8                insert date
alt+9                insert time

ctl+1                focus on first editor
ctl+2                focus on next editor
ctl+3                focus on previous editor
ctl+8                focus on explorer pane
ctl+9                focus on github pane    

ctl+alt+x            reload window
ctl+alt+u            unfold all code
ctl+alt+f            fold code level 2 (rivt sections visible)
ctl+alt+a            fold code - all levels
ctl+alt+t            toggle local fold
ctl+alt+e            toggle explorer sort order
ctl+alt+s            toggle spell check
ctl+alt+g            next editor group

ctl+shift+u          open URL under cursor in browser
ctl+shift+s          open GitHub rivt README search
ctl+shift+a          commit all 
ctl+shift+z          commit current editor
ctl+shift+x          post to remote   


rivt installation
=================

The minimum software needed to run is:

- Python 3.8 or higher 
- rivt library + Python dependencies

A complete rivt system additionally includes:

- VSCode + extensions 
- LaTeX 
- Github account

rivt-sys installs the complete rivt system in a portable folder via a zip file,
and is available for every OS platform. rivt also runs in the cloud using
GitHub CodeSpaces or other cloud service providers. Installation details are
provided in the [rivt User Manual](https://www.rivt-sys.net>)

'''
