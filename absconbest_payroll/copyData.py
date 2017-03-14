import os
import shutil

# Moving data files into the folder created in Desktop.

# The function parameter is just for convenience. It does
# not mean dir_home is moved. 
def main(dir_home):
    # Make the target directories.
    os.makedirs(dir_home)
    dir_data=os.path.join(dir_home,'data')
    os.makedirs(dir_data)

    # Find the data's location.
    loc_sheet=os.path.dirname(os.path.abspath(__file__))
    loc_logo=os.path.join(
        loc_sheet,
        'logo.png'
    )
    loc_sheet=os.path.join(
        loc_sheet,
        'absconbest_payroll.xlsx'
    )

    # Copy absconbest_payroll.xlsx into the desktop folder.
    shutil.copy2(loc_sheet, dir_home)

    # Copy logo.png into the desktop folder.
    shutil.copy2(loc_logo, dir_data)
