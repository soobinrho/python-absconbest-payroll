Absconbest Payroll/Time Management
==================================

Installation
------------

**Ubuntu/Linux**

This program requires Python2 and its building tools which can be installed with a terminal:

>>> sudo apt update
>>> sudo apt install python-dev

without sudo

>>> pip install --upgrade pip
>>> pip install wheel setuptools   

Finally, install the package:

>>> pip install absconbest_payroll --user

**Windows**

Install Python2's latest version from `here
<https://www.python.org/downloads/release/python-2713/>`_.

Then open a *cmd* and type:

>>> python -m pip install --upgrade pip wheel setuptools
>>> python -m pip install absconbest_payroll

**Function Examples**

Look at your Desktop. There now is an 'absconbest_payroll.xlsx' which is compatible with both Microsoft Excel and Libreoffice Calc.

>>> cd ~/Desktop/absconbest_payroll

Both Excel and Calc work well with our program.

>>> libreoffice absconbest_payroll.xlsx

.. image:: pics/xlsx.png
   :target: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_excel.html


We can customize the xlsx file in any way we want. 
Moreover, we can generate a report and graph by opening a terminal and typing:

>>> absconbest

Using this extra function needs to install *texLive*, which is `here
<https://www.tug.org/texlive/acquire-iso.html>`_.

.. image:: pics/plotly.png
   :target: https://plot.ly

The function now generated the graph and report, which is saved in the desktop folder.

 .. image:: pics/pylatex.png
   :target: https://github.com/JelteF/PyLaTeX

If you want to uninstall, first:

>>> pip uninstall absconbest_payroll -y

Then, for Linux:

>>> rm -rf ~/Desktop/absconbest_payroll/

For Windows, delete the absconbest_payroll folder in the desktop folder.

**Contribution**

We can find our Python source code by: 

>>> ls ~/Download/absconbest_payroll/absconbest_payroll

.. image:: https://cdn.rawgit.com/syl20bnr/spacemacs/442d025779da2f62fc86c2082703697714db6514/assets/spacemacs-badge.svg
   :target: http://spacemacs.org
