.. image:: https://cdn.rawgit.com/syl20bnr/spacemacs/442d025779da2f62fc86c2082703697714db6514/assets/spacemacs-badge.svg
   :target: http://spacemacs.org

Absconbest Payroll/Time Management
==================================

Installation
------------

**Ubuntu/Linux**

This program requires Python2 and its building tools which can be installed with a terminal:

>>> sudo apt update
>>> sudo apt install python-dev python-pip
>>> sudo -H pip install --upgrade pip wheel setuptools

Finally, install our package without *sudo*:

>>> pip install absconbest_payroll --user

**Windows**

Install Python2's latest version `here
<https://www.python.org/downloads/release/python-2713/>`_, and open a *cmd* and install Python's building tools:

>>> python -m pip install --upgrade pip wheel setuptools

Then, install our package:

>>> python -m pip install absconbest_payroll

Function Examples
-----------------

Look at your Desktop. There now is an 'absconbest_payroll.xlsx' which is compatible with both Microsoft Excel and Libreoffice Calc. It works well with both Excel and Calc. In Ubuntu, we can open it with:

>>> libreoffice ~/Desktop/absconbest_payroll/absconbest_payroll.xlsx

.. image:: pics/xlsx.png
   :target: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_excel.html


We can customize the xlsx file in any way we want. 

Moreover, we can generate a report and graph. Using this extra function needs to install *texLive* `here
<https://www.tug.org/texlive/acquire-iso.html>`_.

In Ubuntu, open a terminal and type the following command:

>>> absconbest

Or in Windows, click *absconbest.exe*.

.. image:: pics/plotly.png
   :target: https://plot.ly

The function now generated the graph and report, which is saved in the desktop folder.

 .. image:: pics/pylatex.png
   :target: https://github.com/JelteF/PyLaTeX

If you want to uninstall, first:

>>> pip uninstall absconbest_payroll -y

Then, for Ubuntu:

>>> rm -rf ~/Desktop/absconbest_payroll/

For Windows, delete the absconbest_payroll folder in the desktop folder.

**Contribution**

We can find our Python source code by: 

>>> ls ~/Download/absconbest_payroll/absconbest_payroll

