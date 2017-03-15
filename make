#!/bin/bash 
trash dist/*
python setup.py sdist
python setup.py bdist_wheel rotate -d dist/ -m .whl,.tar.gz -k 2
sudo -H pip uninstall absconbest_payroll -y
sudo -H pip install dist/*.whl
# This requires sudo apt install trash
trash -rf *.egg-info build absconbest_payroll/*.pyc
echo twine upload "dist/*" for PyPI

