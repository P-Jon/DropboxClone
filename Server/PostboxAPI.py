from flask import Flask

app = Flask(__name__)

@app.route("/")
def default_route():
    return "<p> Default Route </p>"

# Validation Routes
## Checking if the data from the client matches that of the server

## - Validate Directory Contents -
@app.route("/validate_directories")
def validate_directory_contents(file_list):
    ''' 
    Expecting data from a list of files

    Arguments:

    file_list: Data regarding all files in source directory.

    Returns: Format of [[entry, true/false], [entry,true/false], . . .] as to whether it is current or not.
    '''
    return "<p> VD Route </p>"



## - Validate File Contents -
@app.route("validate_file")
def validate_file_contents(file):
    ''' 
    Expecting data from a single file

    Arguments:

    file: Data regarding target file in source directory.

    Returns: true if file is current, false if not.
    '''
    return "<p> VF Route </p>"

# Upload Routes

