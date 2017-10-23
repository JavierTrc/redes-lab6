import sys
import socketserver
import clientHandler
import threading
import os
import socket


class UDPServer(socketserver.ThreadingUDPServer):

    def __init__(self, address, handler, max_clients=1000):
        super().__init__(address, handler)
        self.current_clients = 0
        self.max_clients = max_clients

    def service_actions(self):
        self.current_clients = threading.active_count() - 1

    def verify_request(self, request, client_address):
        if self.current_clients == self.max_clients:
            return False
        else:
            return True


def main(PORT):

    HOST = "localhost"

    server = UDPServer((HOST, PORT), clientHandler.UDPClientHandler)

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    try:
        print("Server loop running in thread")
        server.serve_forever()
    except KeyboardInterrupt:
        print("Forced server to close")
    finally:
        server.shutdown()


if __name__ == "__main__":
    PORT = int(sys.argv[1])
    main(PORT)
