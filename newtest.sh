#!/bin/bash

if which python > /dev/null 2>&1;
then
    #Python is installed
    python_version=`python --version 2>&1 | awk '{print $2}'`
    echo "Python version $python_version is installed."

else
    #Python is not installed
    echo "No Python executable is found."
fi
