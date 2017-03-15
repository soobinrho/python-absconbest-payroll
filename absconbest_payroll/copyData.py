import os
import shutil

# Moving data files into the folder created in Desktop.

# The function parameter is just for convenience. It does
# not mean dir_home is moved. 
def main(dir_home):
    # Make the target directories.
    os.makedirs(dir_home)
    dir_output=os.path.join(dir_home,'output')
    os.makedirs(dir_output)

    loc_sheet=os.path.join(
        loc_sheet,
        'absconbest_payroll.xlsx'
    )

    # Copy absconbest_payroll.xlsx into the desktop folder.
    shutil.copy2(loc_sheet, dir_home)
