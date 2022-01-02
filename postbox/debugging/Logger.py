from postbox.helper.YAMLHandler import YAMLHandler
class Logger():
    def __init__(self, type):
        '''
        Variable 'Type' is whether the logger is handling client or server debugging
        and adjusts to using the relevant configuration.
        '''
        self.config_type = "server"
        self.debug_mode = False
        self.get_config()
    
    def get_config(self):
        dbm = YAMLHandler().get_variable(self.config_type + "_debug_mode") # Warning: can be set to None.
        if (dbm != None):
            self.debug_mode = dbm

    def msg(self, message):
        if (self.debug_mode):
            print(message)