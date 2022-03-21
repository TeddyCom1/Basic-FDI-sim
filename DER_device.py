from socket import *
import sys
from threading import Thread

class ClientThread(Thread):
    def __init__(self, clientAddress, clientSocket):
        Thread.__init__(self)
        self.clientAddress = clientAddress
        self.clientSocket = clientSocket
        self.clientAlive = True
        
    def run(self):
        pass

    def communicate(self, message):
        self.clientSocket.send(message.encode())

    