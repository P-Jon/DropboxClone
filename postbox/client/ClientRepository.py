import requests

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
            print("woo")
        else:
            print("boo")

    def send_files(self):
        pass

    def request_file_validation(self):
        pass

    def get_server_metadata(self):
        pass
