import sys
import socket
import time


def handler(sock, address, num_mens):
    for i in range(1, num_mens + 1):
        timestamp_ms = time.time() * 1000
        msj = "{0};{1}".format(i, timestamp_ms)
        sock.sendto(bytes(msj, "utf-8"), address)


def client(ip, port, num_obj=5):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        handler(sock, (ip, port), num_obj)


if __name__ == "__main__":
    IP, PORT = sys.argv[1], int(sys.argv[2])
    client(IP, PORT)
