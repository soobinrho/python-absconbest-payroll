import os

# The first time our package is installed, it creates
# a folder in Desktop. Then, it moves absconbest_payroll.xlsx
# into the created folder.
dir_home=os.path.join('~','Desktop','absconbest_payroll')
dir_home=os.path.expanduser(dir_home)

if not os.path.exists(dir_home):
   copySpreadsheet.main(dir_home)

#import absconbest_payroll.__main__

