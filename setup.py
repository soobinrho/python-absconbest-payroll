import os
from setuptools import setup
import pwd
import grp


#Following the API setuptools' standards
setup(
    name='absconbest-payroll',
    version='1.42',
    description='An open-source spreadsheet compatible with both Excel and Calc; and functions for the best time/payroll management',
    long_description='An open source time/payroll management system including a spreadsheet working perfectly with both Excel and Calc; and functions like generating a graph and report; tested and worked well in Ubuntu 16.04 and Windows 10; https://github.com/soorho/absconbest-payroll',
    url='https://github.com/soorho/absconbest-payroll',
    author='Soobin Rho',
    author_email='soobinrho@gmail.com',
    license='MIT',
    packages=['absconbest_payroll'],
    include_package_data=True,
    install_requires=[
        'pandas',
        'plotly',
        'pylatex',
        'xlrd',
        'schedule',
        'ipython',
        'numpy',
    ],
    platforms=[
        'Linux',
        'Windows'
    ],
    entry_points={
        'gui_scripts': [
            'absconbest=absconbest_payroll.commands:main',
        ],
    },
    package_dir={'absconbest_payroll': 'absconbest_payroll'},
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Development Status :: 5 - Production/Stable',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'Topic :: Office/Business :: Office Suites',
        'Topic :: Office/Business :: Scheduling',
        'Topic :: Utilities',
    ],
    keywords='time payroll management',

    #Include Data
    package_data={'': [
        'logo.png', 'absconbest_payroll.xlsx'
    ]},
)

# # If the user installed absconbest_payroll with sudo by 
# # mistake, we had better change absconbest_payroll.xlsx's
# # ownership to the user's not root's.
# uid = pwd.getpwnam(os.path.split(os.path.expanduser('~'))[-1]).pw_uid
# gid = grp.getgrnam("nogroup").gr_gid
# os.chown(dir_home, uid, gid)
# os.chown(dir_home+'absconbest_payroll.xlsx', uid, gid)
