from postbox.helper.YAMLHandler import YAMLHandler
class Logger():
    def __init__(self):
        self.debug_mode = False
        self.get_config()
    
    def get_config(self):
        dbm = YAMLHandler().get_variable("debug_mode") # Warning: can be set to None.
        if (dbm != None):
            self.debug_mode = dbm

    def msg(self, message):
        if (self.debug_mode):
            print("[DEBUG] " + message)