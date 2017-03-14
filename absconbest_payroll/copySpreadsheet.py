import os
import shutil

# Moving absconbest_payroll.xlsx to the folder created
# in Desktop.

# The function parameter is just for convenience. It does
# not mean dir_home is moved. Instead, we will move dir_xlsx.
def main(dir_home):
    # First, find where absconbest_payroll.xlsx is.
    dir_xlsx=os.path.dirname(__file__)
    dir_xlsx=os.path.join(dir_xlsx,'absconbest_payroll.xlsx')

    # Copy absconbest_payroll.xlsx into the desktop folder.
    shutil.copy2(dir_xlsx, dir_home)
