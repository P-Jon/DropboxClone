# Dropbox Clone

This is a dropbox clone made using Python, with the goal of synchronising a destination folder, with a source folder over IP - similarly to how OneDrive and Dropbox operate.

This solution implements a client and server model with test folders and unit testing.

## How to Use
To get the packages used in this project, it is advised to use a Python virtual environment and run, in the parent directory:
    
    pip install -e .
    pip install -r requirements.txt

This was built, tested and run on a Windows 10 machine. Currently, it has not been tested on other operating systems however outside of configured variables in the yaml and tests,
it should work as intended.
