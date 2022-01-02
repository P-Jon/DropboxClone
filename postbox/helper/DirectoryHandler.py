import json
import base64

from os import listdir, path
from postbox.models.Metadata import Metadata

class DirectoryHandler():
    '''
    This class is designed to handle all functionality actually involving
    directories and handling files or file data. 
    '''
    def __init__(self) -> None:
        pass

    def get_file_metadata(self, dir):
        file_metadata = []

        for file in listdir(dir):
            dir_path = path.join(dir, file)
            metadata = Metadata(file, path.getsize(dir_path), path.getmtime(dir_path))
            file_metadata.append(json.dumps(metadata.__dict__))

        file_metadata = "{ \"files\": [ "  + ', '.join(file_metadata) + "] }"
        return file_metadata

    # This was taken & amended as an example of how people were handling files with flask
    # https://docs.faculty.ai/user-guide/apis/flask_apis/flask_file_upload_download.html
    # Left it in as it could prove useful for lazily grabbing filenames
    # Could just be extra technical debt though...
    def list_filenames(self, dir):
        """Endpoint to list filenames on the server."""
        return listdir(dir)

    def detect_change(self, f1, f2):
        '''
        Detecting whether a change has been made between the files.
        Based on file size and last update time.
        '''
        return f1.get_similarity(f2)

    # Section: Getting and Writing files
    # Desc:    Actually returning or saving file data

    def get_file(self, dir, filename):
        file = None
        p = path.join(dir, filename)

        if path.isfile(p):
            with open(p, "rb") as fp: # Read in Binary mode
                file = fp.read()
            print(filename)
            file = base64.b64encode(file) # Ensuring that files are encoded as expected
            file = [filename, file.decode('ascii')]
            print(file)
            return file
        else:
            return None

    # Going to grab all the files and then let the API interface handle
    # transforming it to send.
    def get_files(self, dir):
        files = []
        for filename in listdir(dir):
                file = self.get_file(dir,filename)
                if file is not None:
                    files.append(file)
        return files

    def write_file(self, dir, file):
        filename = file.filename
        with open(path.join(dir, filename), "wb") as fp:
            fp.write(file.data)
        return 200    