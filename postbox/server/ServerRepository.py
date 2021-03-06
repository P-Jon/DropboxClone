from postbox.debugging.Logger import Logger
from postbox.helper.DirectoryHandler import DirectoryHandler
from postbox.helper.YAMLHandler import YAMLHandler
from postbox.models.Metadata import Metadata

# Note:
# In the future it would be more effective to use a package such as jsonpickle to handle complex
# JSON structures.

class Server():
    '''
    Description: Class that acts as a business logic API for any server-side logic, currently it only
                 contains logic that could arguably be shared with the client. The goal however is to be
                 extensible without the client relying upon whatever is implemented here. 
                 Single Responsibility Principle / Interface Segregation Principle
    '''
    def __init__(self):
        self.directory = None
        self.dir_handler = DirectoryHandler()
        self.logger = Logger()
        self.load_config()

    def load_config(self):
        yaml_handler = YAMLHandler()
        self.directory = yaml_handler.get_variable('source_directory')
    
    def get_file_metadata(self):
        return self.dir_handler.get_file_metadata(self.directory)
    
    def list_filenames(self):
        return self.dir_handler.list_filenames(self.directory)

    def get_files(self):
        return self.dir_handler.get_files(self.directory)

    def get_file(self, filename):
        return self.dir_handler.get_file(self.directory, filename)

    def save_file(self, file):
        self.logger.msg(f"Writing file to dir: {self.directory}")
        self.dir_handler.write_file(self.directory, file)

    def save_files(self, files):
        self.logger.msg(f"Saving files...")
        self.dir_handler.write_files(self.directory, files)

    def remove_file(self, filename):
        self.logger.msg(f"Removing file '{filename}' from server.")
        self.dir_handler.remove_file(self.directory, filename)

    def remove_files(self, filenames):
        self.logger.msg("Removing files from server")
        self.dir_handler.remove_files(self.directory, filenames)