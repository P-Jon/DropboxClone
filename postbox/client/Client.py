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
        self.repository.welcome_client()
        self.repository.present_directory()
        self.cached_metadata = self.repository.get_client_metadata() # Caching on instantiation
        self.frontend_loop()

    # https://stackoverflow.com/questions/5852981/python-how-do-i-display-a-timer-in-a-terminal
    def timer(self, wait_time):
        for remaining in range(wait_time, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write("{:2d}s until next check...".format(remaining))
            sys.stdout.flush()
            time.sleep(1)

    def frontend_loop(self):
        max_time = 300 # Maximum backoff wait is 300 seconds.
        backoff_increment = 10
        wait_time = 20

        while(True):
            self.timer(wait_time)
            check_match = self.repository.check_metadata_match(self.cached_metadata)
            if (check_match == False):
                print("\nChange in directory detected")
                self.repository.present_directory()
                self.cached_metadata = self.repository.get_client_metadata()
                self.repository.send_files()
                wait_time = 20
            else:
                if (wait_time <= max_time):
                    wait_time += backoff_increment