import yaml 

class YAMLHandler():
    def __init__(self) -> None:
        pass

    def get_variable(self, variable):
        config = None
        with open('config.yml', 'r') as stream:
            config = yaml.safe_load(stream)
        
        if config != None:
            return config[variable]
        else:
            return None