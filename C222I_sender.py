import json
import socket


def enc(msg, key):
    m = 8361532
    a = 873675
    c = 72346
    seed = key
    data = []
    for ch in msg:
        seed = (a * seed + c) % m
        data.append(ord(ch) ^ seed)
    return data


if __name__ == '__main__':
    key = 31337
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 50007))
    msg = 1
    while msg:
        msg = input('Message: ')
        data = enc(msg, key)
        s.sendall(json.dumps(data))
