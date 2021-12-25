from os import listdir, stat, path

import json
import yaml

from Models.Metadata import Metadata

class Server():
    def __init__(self):
        self.directory = None
        self.load_config()

    def load_config(self):
        config = None
        with open('config.yml', 'r') as stream:
            config = yaml.safe_load(stream)
        
        if config != None:
            self.directory = config['source_directory']

    def get_file_metadata(self):
        file_metadata = []

        for file in listdir(self.directory):
            dir_path = path.join(self.directory, file)
            metadata = Metadata(file, path.getsize(dir_path), path.getmtime(dir_path))
            file_metadata.append(json.dumps(metadata.__dict__))

        return file_metadata