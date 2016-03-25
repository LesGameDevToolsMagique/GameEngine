import sys
import SocketServer

class MyTCPHandler(SocketServer.BaseRequestHandler):

    # Override to handle connection with clients
    def handle(self):
        self.data = self.request.recv(4096).strip()

        # just send back the same data to all client
        self.request.sendall(self.data)
