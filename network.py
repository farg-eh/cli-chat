import socket
from support import *


class NetworkManager:
    def __init__(self):
        # settings
        self.boradcast = False
        self.search = False

        # info
        self.my_ip = get_my_ip()

        # clients
        self.clients = []



    def handle_client(client_socket, addr, name):
        pass

    def update(self):
        pass
