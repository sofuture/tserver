#!/usr/bin/env python

import argparse
import socket
import sys
sys.path.append('gen-py')

from helloworld import HelloWorld
from helloworld.ttypes import *
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class HelloWorldHandler(object):
    def __init__(self):
        self.log = {}

    def ping(self):
        print "ping()"

    def sayHello(self):
        print "sayHello()"
        return "say hello from {}".format(socket.gethostbyname(socket.gethostname()))

    def sayMsg(self, msg):
        print "sayMsg({})".format(msg)
        return "say {} from {}".format(msg, socket.gethostbyname(socket.gethostname()))


if __name__ == '__main__':
    parser = argparse.ArgumentParser("helloworld thrift server")
    parser.add_argument('port', metavar='port', type=int, help='port to listen on')

    args = parser.parse_args()

    handler = HelloWorldHandler()
    processor = HelloWorld.Processor(handler)
    transport = TSocket.TServerSocket(port=args.port)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print "Starting server..."

    try:
        server.serve()
    except KeyboardInterrupt:
        pass

    print "done!"

