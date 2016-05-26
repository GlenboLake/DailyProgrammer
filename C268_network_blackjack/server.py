import socket
import threading

import time

class _ClientMetadata(object):
    def __init__(self, name):
        self.name = name
        self.ready = False
        self.cards = []


class Server(object):
    HOST = ''
    PORT = 4536

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = {}
        self.buf = b''

    def heartbeat(self):
        while True:
            for name, conn in self.clients.copy().items():
                try:
                    self._send_msg('Ding!', conn)
                except ConnectionError:
                    conn.close()
                    self.clients.pop(name)
                    print('Removed {} from clients'.format(name))
            time.sleep(1)

    @staticmethod
    def _send_msg(msg, conn):
        conn.send((msg+'\0').encode())

    def handle_connection(self, conn):
        with conn:
            while True:
                try:
                    self.buf += conn.recv(4096)
                    while b'\0' in self.buf:
                        data = self.buf[:self.buf.index(b'\0')].decode()
                        self.parse_command(data, conn)
                        self.buf = self.buf[self.buf.index(b'\0')+1:]
                except ConnectionError:
                    break

    def parse_command(self, data, conn):
        args = data.split('\t')
        command = args[0]
        if command == 'IDENTIFY':
            name = args[1]
            print('New connection from {}'.format(name))
            self.clients[name] = conn
        elif command == 'LIST':
            print('Received LIST command')
            self._send_msg('\n'.join(sorted(self.clients.keys())), conn)
        elif command == 'BROADCAST':
            message = args[1]
            print('BROADCASTING "{}"'.format(message))
            for conn in self.clients.values():
                self._send_msg(args[1], conn)
        elif command == 'RELAY':
            recipient = self.clients.get(args[1])
            message = args[2]
            print('RELAY "{}" to {}'.format(message, args[1]))
            self._send_msg(message, recipient)
        else:
            print('Unknown command: {}'.format(command))

    def serve(self):
        with self.sock:
            self.sock.bind((self.HOST, self.PORT))
            self.sock.listen()
            print('Server started')
            t = threading.Thread(target=self.heartbeat)
            t.start()
            while True:
                conn, address = self.sock.accept()
                threading.Thread(target=self.handle_connection, args=[conn]).start()


if __name__ == '__main__':
    Server().serve()
