import socket
import threading
import pickle
import time

class Socket:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.data={}
        self.signal=True

    def receive(self):
        while self.signal:
            try:

                self.data=pickle.loads(self.sock.recv(4096))
                # self.data=self.sock.recv(4096)
            except:
                print("You have been disconnected from the server")
                self.signal = False
            break
    def connect(self,ip,host):
        try:
            self.sock.connect((ip,host))

        except:
            print("Could not make a connection to the server")

    def request(self,user,notifier):


        # generare nr

        data="User "+str(notifier)+" "+user
        self.sock.send(str.encode(data))
        time.sleep(0.5)
        self.receive()
    def disconnect(self):
        self.sock.close()

    def getData(self):
        return self.data
#
# a=Socket()
# a.connect('100.101.133.182',23)
# a.request()
# time.sleep(1)
# a.request()
# time.sleep(1)
# a.request()
# time.sleep(1)
# a.disconnect()
# time.sleep(10)
# print("disconnected")
