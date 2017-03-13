Absconbest Payroll/Time Management
==================================

Documentation for Ubuntu/Linux
------------------------------

**Installation**

This program requires Python and its package manager which can be installed by opening a terminal and typing:

>>> sudo apt install python-dev python-pip

We can use an extra function that generates a graph and report. If you want it, install:

>>> sudo apt install texlive-latex-recommended

First, extract the compressed file downloaded.

Last, install the package with a shell:

>>> sudo python setup.py install --user

**Example**

Look at your Desktop. There now is an 'absconbest_payroll.xlsx' which is compatible with both Microsoft Excel and Libreoffice Calc.

>>> cd ~/Desktop/absconbest_payroll

Both Excel and Calc work well with our program.

>>> libreoffice absconbest_payroll.xlsx

.. image:: pics/xlsx.png
   :target: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_excel.html


We can customize the xlsx file in any way we want. 
Moreover, if you installed *texLive* we can generate a report and graph by opening a terminal and typing:

>>> generateAbsconbest

.. image:: pics/plotly.png
   :target: https://plot.ly

The function now generated the graph and report, which is saved in the desktop folder.

 .. image:: pics/pylatex.png
   :target: https://github.com/JelteF/PyLaTeX

If you want to uninstall:

>>> sudo pip uninstall absconbest_payroll
>>> rm -rf ~/Desktop/absconbest_payroll/

**Contribution**

We can find our Python source code by: 

>>> ls ~/Download/absconbest_payroll/absconbest_payroll

.. image:: https://cdn.rawgit.com/syl20bnr/spacemacs/442d025779da2f62fc86c2082703697714db6514/assets/spacemacs-badge.svg
   :target: http://spacemacs.org
