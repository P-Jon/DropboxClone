from postbox.client.ClientRepository import ClientRepository

import time
import sys 

class Client():
    '''
    The 'frontend' of the clientside - controlling how the application
    is presented and functions with the user.
    '''
    def __init__(self):
        self.repository = ClientRepository()

        self.repository_setup()
        self.cached_metadata = self.repository.get_client_metadata() # Caching on instantiation
        
        self.frontend_loop()

    def repository_setup(self):
        self.repository.setup()
        self.repository.welcome_client()
        self.repository.present_directory()
        
    # https://stackoverflow.com/questions/5852981/python-how-do-i-display-a-timer-in-a-terminal
    def timer(self, wait_time):
        for remaining in range(wait_time, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write("{:2d}s until next check...".format(remaining))
            sys.stdout.flush()
            time.sleep(1)

    def send_files_procedure(self, filenames):
        print("\nChange in directory detected")
        self.repository.present_directory()
        self.cached_metadata = self.repository.get_client_metadata()
        if (len(filenames) > 0):
            self.repository.send_files(filenames)
        else:
            self.repository.send_all_files()

    def frontend_loop(self):
        max_time = 300 # Maximum backoff wait is 300 seconds.
        backoff_increment = 10
        wait_time = 20

        while(True):
            self.timer(wait_time)
            increment_timer = True
            deleted_files = self.repository.check_deletions(self.cached_metadata)
            if len(deleted_files) > 0:
                self.repository.delete_files(deleted_files)
                wait_time = 20
                increment_timer = False

            new_flag, filenames = self.repository.check_new_files(self.cached_metadata)
            if (new_flag == False):
                self.send_files_procedure(filenames)
                wait_time = 20
                increment_timer = False

            check_match, filenames = self.repository.check_metadata(self.cached_metadata)
            if (check_match == False):
                self.send_files_procedure(filenames)
                wait_time = 20
                increment_timer = False
                
            if (increment_timer):
                if (wait_time <= max_time):
                    wait_time += backoff_increment