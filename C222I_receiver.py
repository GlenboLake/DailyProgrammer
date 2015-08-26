import json
import socket


def dec(msg, key):
    m = 8361532
    a = 873675
    c = 72346
    seed = key
    data = ''
    for ch in msg:
        seed = (a * seed + c) % m
        data += chr(ch ^ seed)
    return data


if __name__ == '__main__':
    key = 31337
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 50007))
    s.listen(1)
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        if data:
            print(dec(json.loads(data), key))
        else:
            print('<done>')
            break
