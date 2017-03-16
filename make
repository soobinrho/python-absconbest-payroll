#!/bin/bash
# I said on the doc that the GNU make works, but I have to learn how to use it. Sorry.
# We can use this with ./makefile
rm dist/*
python setup.py sdist bdist_wheel rotate -d dist/ -m .whl,.tar.gz -k 2
sudo -H pip uninstall absconbest_payroll -y
sudo -H pip install dist/*.whl
echo "This is echo!" twine upload "dist/*" for PyPI

