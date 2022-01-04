from flask import Flask, request
from flask.json import jsonify
from flask.wrappers import Response
from postbox.server.ServerRepository import Server

app = Flask(__name__)
server = Server()

# Default
@app.route("/")
def default_route():
    return "<p> Default Route </p>"

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
        return Response(files, status=200, mimetype='text/json')
    else:
        return None, 204

@app.route("/get_file/<path:path>", methods=["GET"])
def get_file(path):
    file = server.get_file(path)
    if file != None:
        return jsonify({'files:':file})

# Upload Routes
@app.route("/upload_multiple_files", methods=["POST"])
def upload_multiple_files():
    '''
    Sending a list of files to the server to update or upload (C)R(U)D to the directory.    
    '''
    files = request.get_json()
    server.save_files(files)
    #files[0].filename
    return "<p> UM Files </p>", 201

@app.route("/upload_file/<path:path>", methods=["POST"])
def upload_file(path):
    '''
    Sending a file to the server to update or upload (C)R(U)D to the directory.
    '''
    return "<p> Upload File </p>", 201

# Destroy Routes
@app.route("/remove_file/<path:path>", methods=["POST"])
def delete_file(path):
    server.remove_file(path)
    return 200

@app.route("/remove_multiple_files", methods=["POST"])
def delete_multiple_files():
    filenames = request.get_json()
    server.remove_files(filenames)
    return 200

# Error Handling
@app.errorhandler(404)
def resource_not_found(error):
    return "<h1> 404 Not Found </h1>", 404

@app.route("/list-filenames")
def list_filenames():
    """Endpoint to list filenames on the server."""
    files = server.list_filenames()
    return jsonify(files), 200