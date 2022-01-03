import requests

from postbox.helper.DirectoryHandler import DirectoryHandler
from postbox.debugging.Logger import Logger
from postbox.helper.YAMLHandler import YAMLHandler as yh

class ClientRepository():
    '''
    Implementing the 'backend' of the clientside code,
    handling any interfacing with the Postbox Service API.

    Additionally, this will handle file handling logic.
    '''
    def __init__(self):
        self.directory = None
        self.api_addr = None
        self.config_set = False
        self.logger = Logger()
        self.dir_handler = DirectoryHandler()
        self.load_config()

    def load_config(self):
        yaml_handler = yh()
        self.directory = yaml_handler.get_variable('source_directory')
        self.api_addr = yaml_handler.get_variable('api_addr')
        self.config_set = True

    # Print out the directory in the CLI
    def present_directory(self):
        pass
    
    # Welcome the Client and present some CLI
    def welcome_client(self):
        print("\n--- POSTBOX SERVICE ---\n")
        if self.config_set == True:
            print("Configuration Found.")
            print("Local Directory: " + self.directory)
            print("Postbox API Address: " + self.api_addr)
        else:
            print("No configuration found...")
        print("\n----------------------\n")

    # https://docs.python-requests.org/en/latest/user/quickstart/#post-a-multipart-encoded-file
    def request_files(self):
        r = requests.get(self.api_addr + "get_directory_files")
        if (r.status_code == 200):
            files_json = r.json()
            self.logger.msg(f"Files successfully retrieved: HTTP {r.status_code}")
            self.dir_handler.write_files(self.directory,files_json)
            self.logger.msg("Files written to directory.")
        else:
            self.logger.msg(f"Fails failed to be retrieved: HTTP {r.status_code}")

    def send_files(self):
        files = self.dir_handler.get_files(self.directory)
        r = requests.post(self.api_addr + "upload_multiple_files", json=files)
        if (r.status_code == 201):
            self.logger.msg("Send files was successful")
        else:
            self.logger.msg(f"Send files was not successful: HTTP {r.status_code}")

    def request_file_validation(self):
        pass

    def get_server_metadata(self):
        pass
