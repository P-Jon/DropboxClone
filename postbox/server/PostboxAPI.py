from flask import Flask, request
from flask.json import jsonify
from flask.wrappers import Response

from postbox.server.ServerLogic import Server

app = Flask(__name__)
server = Server()

# Default
@app.route("/")
def default_route():
    return "<p> Default Route </p>"

# Validation Routes
## Checking if the data from the client matches that of the server

@app.route("/validate_directories", methods=["GET", "POST"])
def validate_directory_contents():
     ''' 
     [POST] Expecting data from a list of files
     Arguments:
     file_list: Data regarding all files in source directory.
     [GET] Returns: Format of [[entry, FILESTATE], [entry,FILESTATE], . . .] as to whether it is current or not.
     '''
     if request.method == "GET":
         return "GET INV",200
     else:
         return "<p> VD Route </p>",200

@app.route("/validate_file/<path:path>", methods=["GET", "POST"])
def validate_file_contents(path):
    ''' 
    [POST] 
    Expecting data from a single file
    Arguments:
    file: Data regarding target file in source directory.
    [GET] 
    Returns: true if file is current, false if not.
    '''
    if request.method == "GET":
        return "<p> GET </p>"
    else:
        return "<p> VF Route </p>"

# Metadata
@app.route("/server_dir_metadata", methods=["GET"])
def get_server_dir_metadata():
     '''
     Returns: JSON list of file metadata on the server.
     '''
     file_metadata = server.get_file_metadata()
     if file_metadata != None:
         return Response(file_metadata, status=200, mimetype='text/json')
     else:
         return 204

# Read Routes
@app.route("/get_directory_files", methods=["GET"])
def get_directory_files():
    files = server.get_files()
    if files != None:
        print(files)
        return jsonify({'files':files}), 200
    else:
        return None, 204

# Upload Routes
@app.route("/upload_multiple_files", methods=["POST"])
def upload_multiple_files():
    '''
    Sending a list of files to the server to update or upload (C)R(U)D to the directory.    
    '''
    files = request.files.getlist("file[]")
    server.save_files(files)
    #files[0].filename
    return "<p> UM Files </p>", 201

@app.route("/upload_file", methods=["POST"])
def upload_file():
    '''
    Sending a file to the server to update or upload (C)R(U)D to the directory.
    '''
    return "<p> Upload File </p>", 201

# Destroy Routes
@app.route("/remove_file/<path:path>", methods=["POST"])
def delete_file(path):
     return None

@app.route("/remove_multiple_files", methods=["POST"])
def delete_multiple_files():
     return None

# Error Handling
@app.errorhandler(404)
def resource_not_found(error):
    return "<h1> 404 Not Found </h1>", 404

@app.route("/list-filenames")
def list_filenames():
    """Endpoint to list filenames on the server."""
    files = server.list_filenames()
    return jsonify(files), 200