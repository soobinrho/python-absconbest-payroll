import os
from setuptools import setup
import pwd
import grp


#Following the API setuptools' standards
setup(
    name='absconbest_payroll',
    version='0.1b1',
    description='Time and payroll management with an xlsx file which works perfectly with both Excel and Calc, also with extra Python functions',
    url='https://github.com/soorho/absconbest_payroll',
    author='Soobin Rho',
    author_email='soobinrho@gmail.com',
    license='MIT',
    packages=['absconbest_payroll'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'absconbest=absconbest_payroll.commands:main',
        ],
    },
    package_dir={'absconbest_payroll': 'absconbest_payroll'},
    install_requires=[
        'pandas',
        'plotly',
        'pylatex',
        'xlrd',
        'ipython',
        'numpy',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Office/Business :: Office Suites',
        'Topic :: Office/Business :: Scheduling',
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
