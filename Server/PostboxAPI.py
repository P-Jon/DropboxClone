from flask import Flask, request
from os import listdir, stat, path

import json
import yaml

from Models.Metadata import Metadata

app = Flask(__name__)

# Config and Setup

directory = None

def load_config():
    config = None
    with open('config.yml', 'r') as stream:
        config = yaml.safe_load(stream)
    
    directory = config['source_directory']

# Default

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
        return "GET INV",200
    else:
        return "<p> VD Route </p>",200

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

# Metadata
@app.route("/server_dir_metadata", methods=['GET'])
def get_server_dir_metadata():
    '''
    Returns: JSON list of file metadata on the server.
    '''
    file_metadata = []

    for file in listdir(directory):
        dir_path = path.join(directory, file)
        metadata = Metadata(file, path.getsize(dir_path), path.getmtime(dir_path))
        file_metadata.append(json.dumps(metadata.__dict__))

    if file_metadata.count > 0:
        return file_metadata, 200 # Need to brush up on how Python serializes objects to JSON. 
    else:
        return 204

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


# Error Handling
@app.errorhandler(404)
def resource_not_found(error):
    return "<h1> 404 Not Found </h1>", 404