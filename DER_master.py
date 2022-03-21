from socket import *
from threading import Thread
import sys

serverHost = "127.0.0.1"
serverPort = int(sys.argv[1])
block_duration = int(sys.argv[2])
client_timeout = int(sys.argv[3])
serverAddress = (serverHost, serverPort)

# define socket for the server side and bind address
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(serverAddress)

clients = []

class ClientThread(Thread):
    def __init__(self, clientAddress, clientSocket):
        Thread.__init__(self)
        clients.append(self)

    def run(self):
        pass

    def rec_data(self):
        pass

    def display_data(self):
        pass

print("\n===== Server is running =====")
print("===== Waiting for connection request from clients...=====")

while True:
    serverSocket.listen()
    clientSockt, clientAddress = serverSocket.accept()
    clientThread = ClientThread(clientAddress, clientSockt)
    clientThread.start()