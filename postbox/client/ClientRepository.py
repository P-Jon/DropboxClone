import json
from os import remove
import requests

from datetime import datetime, timezone
from postbox.helper.DataHandler import DataHandler

from postbox.helper.DirectoryHandler import DirectoryHandler
from postbox.debugging.Logger import Logger
from postbox.helper.YAMLHandler import YAMLHandler as yh
from postbox.models.Metadata import Metadata

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

    def present_directory(self):
        '''
        Print out the directory in the CLI
        '''
        files = self.get_client_metadata()
        print("\n--- CLIENT DIRECTORY ---\n")

        print(" - File - \t\t - Last Modified - \n")
        for file in files:
            time = datetime.fromtimestamp(file.last_edit, tz=timezone.utc).strftime('%Y-%m-%d %H:%M')
            print(f"- {file.filename} \t\t - {time}")
        print("\n----------------------\n")
    
    def welcome_client(self):
        '''
        Welcome the Client and present some CLI
        '''
        print("\n--- POSTBOX SERVICE ---\n")
        if self.config_set == True:
            print("Configuration Found.")
            print("Local Directory: " + self.directory)
            print("Postbox API Address: " + self.api_addr)
        else:
            print("No configuration found...")
        print("\n----------------------\n")

    # Going to ensure the server is up-to-date with the client
    def initial_synchronise(self):
        '''
        Ensuring the server is up to date with the client upon the client joining/re-joining.
        Any files present on the server, but not on the clientside for example will be deleted.
        '''
        local_metadata = self.get_client_metadata()
        server_metadata = self.get_server_metadata()
        pass

    # https://docs.python-requests.org/en/latest/user/quickstart/#post-a-multipart-encoded-file
    def request_files(self):
        '''
        [GET] Requesting files from server to save to client directory.
        '''
        r = requests.get(self.api_addr + "get_directory_files")
        if (r.status_code == 200):
            files_json = r.json()
            self.logger.msg(f"Files successfully retrieved: HTTP {r.status_code}")
            self.dir_handler.write_files(self.directory,files_json)
            self.logger.msg("Files written to directory.")
        else:
            self.logger.msg(f"Fails failed to be retrieved: HTTP {r.status_code}")

    def send_files(self):
        '''
        [POST] Send files from client to server to be saved on the server.
        '''
        files = self.dir_handler.get_files(self.directory)
        r = requests.post(self.api_addr + "upload_multiple_files", json=files)
        if (r.status_code == 201):
            self.logger.msg("Send files was successful")
        else:
            self.logger.msg(f"Send files was not successful: HTTP {r.status_code}")

    def check_deleted_files(self, m1, m2):
        '''
        Checking if any files have been deleted from the directory
        '''
        removed_files = []
        for source_file in m1:
            found = False
            for file in m2:
                if source_file.filename == file.filename:
                    found = True
            
            if found != True:
                removed_files.append(source_file.filename)
        
        r = requests.post(self.api_addr + "remove_multiple_files", json=json.dumps({'filenames':removed_files}))

        if (r.status_code == 200):
            self.logger.msg("Removed files from server")
        else:
            self.logger.msg("Something went wrong when removing files from server")

    def check_metadata_match(self, cached_metadata):
        '''
        Checking if the cached metadata matches the current metadata.
        Returns true if it matches, false if not.
        '''
        metadata = self.get_client_metadata()

        if (len(cached_metadata) != len(metadata)):
            self.check_deleted_files(cached_metadata, metadata)
            return False

        for cached_file in cached_metadata:
            for file in metadata:
                if (cached_file.filename == file.filename):
                    if (cached_file.get_similarity(file) == False):
                        return False

        return True

    def request_file_validation(self):
        pass

    def get_client_metadata(self):
        metadata = self.dir_handler.get_file_metadata(self.directory)
        metadata = json.loads(metadata)
        return DataHandler.strip_metadata_from_json(metadata)

    def get_server_metadata(self):
        r = requests.get(self.api_addr + "server_dir_metadata")
        if (r.status_code == 200):
            self.logger.msg("Got server metadata")
            json_metadata = r.json()
            file_metadata = json.loads(json_metadata)
            return DataHandler.strip_metadata_from_json(file_metadata)
        else:
            self.logger.msg("Failed to get server metadata")
            return None


