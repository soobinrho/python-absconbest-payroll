import os
from absconbest_payroll import copySpreadsheet

def main():
   # The first time our package is installed, it creates
   # a folder in Desktop. Then, it moves
   # absconbest_payroll.xlsx
   # into the created folder.
   dir_home=os.path.join('~','Desktop','absconbest_payroll')
   dir_home=os.path.expanduser(dir_home)+os.sep

   if not os.path.exists(dir_home):
      copySpreadsheet.main(dir_home)

   # Finally, generate a graph and report.
   import absconbest_payroll.__main__

if __name__=="__main__":
   main()
