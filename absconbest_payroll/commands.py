import os
import absconbest_payroll as best

def main():
   # The first time our package is installed, it creates
   # a folder in Desktop. Then, it moves
   # absconbest_payroll.xlsx
   # into the created folder.
   dir_home=os.path.join('~','Desktop','absconbest_payroll')
   dir_home=os.path.expanduser(dir_home)+os.sep

   if not os.path.exists(dir_home):
      best.copySpreadsheet.main(dir_home)

   # Generate a graph and report.
   import absconbest_payroll.__main__

if __name__=="__main__":
   main()
