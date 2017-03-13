Absconbest Payroll/Time Management
==================================

Documentation for Ubuntu/Linux
------------------------------

The xlsx file works well with both MS and Libreoffice. eg)
>>> libreoffice ~/Desktop/absconbest_payroll/absconbest_payroll.xlsx

The program adds a command that generates a report and graph.
>>> generateAbsconbest

The report is saved at
 >>> "~/Desktop/absconbest_payroll/output/"


# *. This program requires Python and its package manager which can be installed by opening a terminal and typing:
sudo apt install python-dev python-pip


First, extract the compressed file.

Last, install the package with a shell:
sudo python setup.py install --user

# Using the program:

# Look at your Desktop.
'Desktop/absconbest_payroll'

# There now is an 'absconbest_payroll.xlsx' which is compatible
# with both Microsoft Excel and Libreoffice Calc.
# The program works perfectly with both.

# We can customize the xlsx file in any way we want. 
# Also, we can generate a report and graph by opening a terminal and typing:
generateAbsconbest

# The function now generated them. The report is saved in
'Desktop/absconbest_payroll/output/'

# The Python source code is located in the 'product' folder we extracted earlier:
'.../product/absconbest_payroll'

# *. To generate a graph with the generateAbsconbest command,
#    We need to install latexlive with a terminal:
sudo apt install

# *. If you want to uninstall:
pip uninstall absconbest_payroll
