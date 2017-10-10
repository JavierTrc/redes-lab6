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
        time_diff = time.time() * 1000 - float(seq[1])
        registry = "{0}:{1} ms".format(seq[0], time_diff)
        print("\n" + registry + "\n")
        with open("registry/" + client, "w+") as f:
            f.write(registry)
