import socket

class SocketClientHandler:

    # Create a socket
    def createSocket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server
    def connectToServer(self, host, port):
        self.socket.connect((host, port))

    # Send data to server
    def sendAll(self, data):
        self.socket.sendall(data)

    # Receive data from server
    def receive(self):
        return self.socket.recv(4096)

    # Close socket
    def close(self):
        self.socket.close()
