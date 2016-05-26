import socket
import threading

import sys


class Client(object):
    HOST = 'localhost'
    PORT = 4536

    def __init__(self, name):
        self.name = name
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _send_msg(self, msg):
        self.sock.send((msg + '\0').encode())

    def connect(self):
        self.sock.setblocking(True)
        self.sock.connect((self.HOST, self.PORT))
        self._send_msg('IDENTIFY\t' + self.name)
        threading.Thread(target=self._listen).start()

    def list_clients(self):
        self._send_msg('LIST')

    def _listen(self):
        data = b''
        while True:
            data += self.sock.recv(4096)
            while b'\0' in data:
                index = data.index(b'\0')
                msg = data[:index].decode()
                data = data[index+1:]
                print(msg)


if __name__ == '__main__':
    client = Client(sys.argv[1])
    client.connect()
    client.list_clients()
