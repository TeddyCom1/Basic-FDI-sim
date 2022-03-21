'''
Created by Calvin Long z5255352 (UNSW)

How to use DER_master.py

python3 DER_master.py ip_address Server_port

e.g.

python3 DER_master.py 127.0.0.1 8081

This code will wait for in comming connections and display the data obtained from the Devices 
'''

from socket import *
from threading import Thread
import sys

serverHost = sys.argv[1]
serverPort = int(sys.argv[2])
serverAddress = (serverHost, serverPort)

# define socket for the server side and bind address
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(serverAddress)

clients = []

class ClientThread(Thread):
    def __init__(self, clientAddress, clientSocket):
        Thread.__init__(self)
        clients.append(self)
        self.clientAddress = clientAddress
        self.clientSocket = clientSocket
        self.clientAlive = True
        

    def run(self):
        data = ''
        while self.clientAlive:
            try:
                data = self.read_data()
            except timeout as e:
                continue
            
            if data == '':
                self.clientAlive = False
                break

            self.display_data(data)
        clients.remove(self)

    def display_data(self, data):
        print(data)

    def read_data(self):
        data = self.clientSocket.recv(1024)
        data = data.decode()
        data = data.rstrip('\n')
        return data

print("\n===== Server is running =====")
print("===== Waiting for connection request from clients...=====")

while True:
    serverSocket.listen()
    clientSockt, clientAddress = serverSocket.accept()
    clientThread = ClientThread(clientAddress, clientSockt)
    clientThread.start()