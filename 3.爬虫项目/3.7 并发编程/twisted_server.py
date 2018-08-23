import sys
from twisted.internet.protocol import ServerFactory
from twisted.protocols.basic import LineReceiver
from twisted.python import log
from twisted.internet import reactor


class CmdProtocol(LineReceiver):
    delimiter = '\n'

    def connectionMade(self):
        self.client_ip = self.transport.getPeer()[1]
        log.msg("Client connection from %s" % self.client_ip)
        if len(self.factory.clients) >= self.factory.clients_max:
            log.msg("Too many connections. bye !")
            self.client_ip = None
            self.transport.loseConnection()
        else:
            self.factory.clients.append(self.client_ip)

    def connectionLost(self, reason):
        log.msg('Lost client connection. Reason: %s' % reason)
        if self.client_ip:
            self.factory.clients.remove(self.client_ip)

    def lineReceived(self, line):
        log.msg('Cmd received from %s : %s' % (self.client_ip, line))


class MyFactory(ServerFactory):
    protocol = CmdProtocol

    def __init__(self, clients_max=10):
        self.clients_max = clients_max
        self.clients = []


log.startLogging(sys.stdout)
reactor.listenTCP(9999, MyFactory(2))
reactor.run()

'''
    2018-08-23 20:49:05+0800 [-] Log opened.
    2018-08-23 20:49:05+0800 [-] MyFactory starting on 9999
    2018-08-23 20:49:05+0800 [-] Starting factory <__main__.MyFactory object at 0x000002C107F72B00>
'''
