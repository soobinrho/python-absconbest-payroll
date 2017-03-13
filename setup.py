import os
from setuptools import setup

dir_home=os.path.expanduser("~/Desktop/absconbest_payroll/")
if not os.path.exists(dir_home):
    os.makedirs(dir_home)

setup(
    name='absconbest_payroll',
    version='0.1b1',
    description='Manages payroll and time',
    url='https://github.com/soorho',
    author='Soooo',
    author_email='soobinrho@gmail.com',
    license='MIT',
    packages=['absconbest_payroll'],
    include_package_data=True,
    scripts=['absconbest_payroll/generateAbsconbest'],
    package_dir={'absconbest_payroll': 'absconbest_payroll'},
    package_data={'absconbest_payroll': ['logo.png']},
    data_files=[
        (dir_home,
         ['absconbest_payroll/absconbest_payroll.xlsx', 'absconbest_payroll/read_cover_page_please.txt'])
    ],
    install_requires=[
        'pylatex',
        'plotly',
        'pandas',
    ],
    zip_safe=False
)
