import json
from os import listdir, path

from Models.Metadata import Metadata

class DirectoryHandler():
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

    def get_files(self, dir):
        return None

    def get_file(self, dir, filename):
        return None