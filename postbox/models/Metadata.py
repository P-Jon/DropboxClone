class Metadata():
    def __init__(self, filename, size, last_edit):
        self.filename = filename
        self.size = size
        self.last_edit = last_edit

    def get_similarity(self, f1):
        '''
        Detecting whether a change has been made between the current file;
        target file. Based on file size and last update time.
        Returns: True if similarity matches, False if not.
        '''
        if (self.size != f1.size or self.last_edit != f1.last_edit):
            return False
        else:
            return True