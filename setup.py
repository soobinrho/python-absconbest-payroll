import os
from setuptools import setup

dir_home=os.path.expanduser("~/Desktop/absconbest_payroll/")
if not os.path.exists(dir_home):
    os.makedirs(dir_home)

setup(
    name='absconbest_payroll',
    version='0.1b1',
    description='Payroll and time management',
    url='https://github.com/soorho/absconbest_payroll',
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
        'python3-dev',
        'pylatex',
        'plotly',
        'pandas',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Office/Business :: Office Suites",
        "Topic :: Office/Business :: Scheduling",
    ],
)
