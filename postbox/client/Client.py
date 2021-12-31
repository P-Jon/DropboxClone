from postbox.helper.YAMLHandler import YAMLHandler as yh

class Client():
    def __init__(self) -> None:
        self.directory = None
        self.api_addr = None
        self.load_config()

    def load_config(self):
        yaml_handler = yh()
        self.directory = yaml_handler.get_variable('source_directory')
        self.api_addr = yaml_handler.get_variable('api_addr')

