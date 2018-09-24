from __future__ import print_function

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class Helloer(DatagramProtocol):
    def startProtocol(self):
        host = "127.0.0.1"
        port = 1245

    def datagramReceived(self, data, addr):
        result = data.decode("utf-8")
        print(result)

    def connectionRefused(self):
        print("No one listening")

# 0 means any port, we don't care in this case
reactor.listenUDP(1234, Helloer())
reactor.run()