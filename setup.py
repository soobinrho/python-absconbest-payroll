import os
from setuptools import setup
import pwd
import grp

dir_home=os.path.expanduser('~/Desktop/absconbest_payroll/')
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
    install_requires=[
        'pandas',
        'plotly',
        'pylatex',
        'xlrd',
        'ipython',
        'numpy',
    ],
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Office/Business :: Office Suites',
        'Topic :: Office/Business :: Scheduling',
    ],

    #Include Data
    package_data={'': ['logo.png']},
    data_files=[
        (
            dir_home,
            ['absconbest_payroll/absconbest_payroll.xlsx'],
        )
    ],
)

uid = pwd.getpwnam(os.path.split(os.path.expanduser('~'))[-1]).pw_uid
gid = grp.getgrnam("nogroup").gr_gid
os.chown(dir_home, uid, gid)
os.chown(dir_home+'absconbest_payroll.xlsx', uid, gid)
