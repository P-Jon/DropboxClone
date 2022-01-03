# Dropbox Clone

This is a dropbox clone made using Python, with the goal of synchronising a destination folder, with a source folder over IP - similarly to how OneDrive and Dropbox operate.

This solution implements a client and server model with test folders and unit testing.

## How to Use
To get the packages used in this project, it is advised to use a Python virtual environment and run, in the parent directory:
    
    pip install -e .
    pip install -r requirements.txt

Be sure to configure each config.yml file according to your preferences as to directory location, correcting the base API address if necessary in the case of the client and selecting whether or not
to show debug messages. 

After this, navigate a CLI instance to the server subdirectory and use:

    $env:FLASK_APP = "PostboxAPI"
    flask run

Now the server is running, the client application can be started, in a new CLI instance, navigate to the client subdirectory and run:

    py t1.py

This may vary from each configuration, i.e. python or python3 instead of py, however that script simply creates an instance of Client, meaning it can also be easily run from the python shell.

Now the program will detect any changes in the client directory and in the event of any changes, it will send the data to the server.

## Notes
This was built, tested and run on a Windows 10 machine. Currently, it has not been tested on other operating systems however outside of configured variables in the yaml and tests,
it should work as intended.
