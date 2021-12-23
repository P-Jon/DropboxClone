from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def default_route():
    return "<p> Default Route </p>"

# Validation Routes
## Checking if the data from the client matches that of the server

## - Validate Directory Contents -
@app.route("/validate_directories", methods=['GET', 'POST'])
def validate_directory_contents():
    ''' 
    [POST] Expecting data from a list of files
    Arguments:
    file_list: Data regarding all files in source directory.

    [GET] Returns: Format of [[entry, FILESTATE], [entry,FILESTATE], . . .] as to whether it is current or not.
    '''
    if request.method == 'GET':
        return "GET INV"
    else:
        return "<p> VD Route </p>"

## - Validate File Contents -
@app.route("/validate_file", methods=['GET','POST'])
def validate_file_contents():
    ''' 
    [POST] 
    Expecting data from a single file
    
    Arguments:
    file: Data regarding target file in source directory.

    [GET] 
    Returns: true if file is current, false if not.
    '''
    if request.method == 'GET':
        return "<p> GET </p>"
    else:
        return "<p> VF Route </p>"

# Upload Routes

@app.route("/upload_multiple_files", methods=['POST'])
def upload_multiple_files():
    '''
    
    '''
    return "<p> UM Files </p>"

@app.route("/upload_file", methods=['POST'])
def upload_file():
    '''
    
    '''
    return "<p> Upload File </p>"

# Destroy Routes
