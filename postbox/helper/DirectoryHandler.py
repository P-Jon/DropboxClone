import json
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
        files = []
        for filename in listdir(dir):
            p = path.join(dir, filename)
            if path.isfile(p):
                files.append(filename)
        return files

    def detect_change(self, f1, f2):
        '''
        Detecting whether a change has been made between the files.
        Based on file size and last update time.
        '''
        return f1.get_similarity(f2)

    def get_files(self, dir):
        return None

    def get_file(self, dir, filename):
        return None

    