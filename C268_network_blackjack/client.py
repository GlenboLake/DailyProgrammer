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

    def _listen(self):
        data = b''
        while True:
            data += self.sock.recv(4096)
            while b'\0' in data:
                index = data.index(b'\0')
                msg = data[:index].decode()
                data = data[index+1:]
                print(msg)

    # Commands
    def list_clients(self):
        self._send_msg('LIST')

    def broadcast(self, message):
        self._send_msg('BROADCAST\t' + message)

    def relay(self, who, message):
        self._send_msg('RELAY\t{}\t{}'.format(who, message))

if __name__ == '__main__':
    client = Client(sys.argv[1])
    client.connect()
    client.list_clients()
    client.broadcast('Hello, world!')
    if len(sys.argv) > 2:
        client.relay(sys.argv[2], "Wassap")
