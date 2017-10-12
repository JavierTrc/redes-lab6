import socketserver
import os
import time


def getFiles(dir):
    return os.listdir("./registry/" + dir)


class UDPClientHandler(socketserver.BaseRequestHandler):
    """Docs of UDPCliet Handler"""

    def handle(self):
        client = self.client_address[0]
        data = str(self.request[0].strip(), "utf-8")
        seq = data.split(";")
        with open("registry/" + client, "a+") as f:
            time_diff = time.time() * 1000 - float(seq[1])
            registry = "{0}:{1} ms\n".format(seq[0], time_diff)
            f.write(registry)
