'''
Created by Calvin Long z5255352 (UNSW)
How to use DER_device.py

Start a DER_master server to accept all the connections

then run:

python3 DER_device.py Address_of_server Port_of_server number_of_devices

e.g.

python3 DER_device.py 127.0.0.1 1234 10

This will automatically connect 10 der devices to DER_master server running
'''


from socket import *
import sys
from threading import Thread
import time

class ClientThread(Thread):
    def __init__(self, clientSocket, serverAddress, client_num):
        Thread.__init__(self)
        self.clientSocket = clientSocket
        self.clientSocket.connect(serverAddress)
        self.clientAlive = True
        self.client_num = client_num

    def run(self):
        while self.clientAlive:
            time.sleep(5)
            self.communicate('Alive!!!')

        self.clientSocket.close()

    def communicate(self, message):
        self.clientSocket.send(('Client '+ str(self.client_num)+ ': '+ message).encode())

    def display_info(self, info):
        print('Client ' + str(self.client_num) + ': ' + info)

serverHost = sys.argv[1]
serverPort = int(sys.argv[2])
number_devices = int(sys.argv[3])

serverAddress = (serverHost, serverPort)

for i in range(0, number_devices):
    client_com = ClientThread(socket(AF_INET, SOCK_STREAM), serverAddress, i)
    client_com.start()