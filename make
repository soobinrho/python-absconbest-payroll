#!/bin/bash
# I said on the doc that the GNU make works, but I have to learn how to use it. Sorry.
# We can use this with ./makefile
trash dist/*
python setup.py sdist
python setup.py bdist_wheel rotate -d dist/ -m .whl,.tar.gz -k 2
sudo -H pip uninstall absconbest_payroll -y
sudo -H pip install dist/*.whl
# This requires sudo apt install trash-cli
trash -rf *.egg-info build
echo "This is echo!" twine upload "dist/*" for PyPI

