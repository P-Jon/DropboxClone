from postbox.client.ClientRepository import ClientRepository


class Client():
    '''
    The 'frontend' of the clientside - controlling how the application
    is presented and functions with the user.
    '''
    def __init__(self) -> None:
        self.repository = ClientRepository()
        self.repository.welcome_client()
        self.repository.request_files()
        self.repository.send_files()