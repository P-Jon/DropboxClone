import yaml

from postbox.helper.DirectoryHandler import DirectoryHandler
from postbox.models.Metadata import Metadata

# Note:
# In the future it would be more effective to use a package such as jsonpickle to handle complex
# JSON structures.

class PBServer():
    def __init__(self):
        self.directory = None
        self.dir_handler = DirectoryHandler()
        self.load_config()

    def load_config(self):
        config = None
        with open('config.yml', 'r') as stream:
            config = yaml.safe_load(stream)
        
        if config != None:
            self.directory = config['source_directory']
    
    def get_file_metadata(self):
        return self.dir_handler.get_file_metadata(self.directory)
    
    def list_filenames(self):
        return self.dir_handler.list_filenames(self.directory)

    def get_files(self):
        return self.dir_handler.get_files(self.directory)

    def get_file(self, filename):
        return self.dir_handler.get_file(self.directory, filename)
