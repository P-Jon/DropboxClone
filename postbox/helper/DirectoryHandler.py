import json
import base64

from os import listdir, path, utime
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
        metadata = self.local_get_file_metadata(dir)
        
        for file in metadata:
            file_metadata.append(json.dumps(file.__dict__))

        file_metadata = "{ \"files\": [ "  + ', '.join(file_metadata) + "] }"
        return file_metadata

    # Hacking this in on limited time, not great from a technical debt perspective.
    def local_get_file_metadata(self,dir):
        file_metadata = []
        for file in listdir(dir):
            dir_path = path.join(dir, file)
            metadata = Metadata(file, path.getsize(dir_path), path.getmtime(dir_path))
            file_metadata.append(metadata)
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

    def compare_metadata(self, m1, m2):
        pass

    # Section: Getting and Writing files
    # Desc:    Actually returning or saving file data

    def get_file(self, dir, filename):
        file = None
        p = path.join(dir, filename)

        if path.isfile(p):
            with open(p, "rb") as fp: # Read in Binary mode
                file = fp.read() 
            #file = base64.b64encode(file) # Tried ensuring that files are encoded as expected
            file = [filename, file.decode('ascii'), path.getatime(p), path.getmtime(p)] # Limitation: Cannot handle files such as PNGs.
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
        return json.dumps({'files':files})

    def write_file(self, dir, file):
        filename = file[0]
        p = path.join(dir, filename)
        with open(p, "wb") as fp:
            f = file[1].encode('ascii')
            fp.write(f)
        
        try:
            utime(p, (file[2],file[3]))
        except:
            return 500
             
        return 200    

    def write_files(self, dir, files):
        files = files.get("files")
        for file in files:
            self.write_file(dir, file)
        return 200