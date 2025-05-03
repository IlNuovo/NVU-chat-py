from threading import Thread
import socket
from time import sleep
from Builder import Structurer


class MultiService:
    def __init__ (Self, s_port : int, srv : str, net = "0.0.0.0"):
        Self.sender = Port(ip_bind=srv, port=s_port)
        pass



class Port (Thread):
    def __init__(Self, group = None, target = None, name = None, args = ..., kwargs = None, *, daemon = None, ip_bind = "0.0.0.0", port : int):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        Self.body = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Self.ip_bind = ip_bind
        Self.port = port
        Self.running = True
        Self.start()

    def run (Self):
        builder = Structurer()

        Self.body.connect((Self.ip_bind, Self.port))
        print (f"added {Self.body}")
        sleep(1)
        Self.body.sendall("connect request -- keep alive".encode('utf-8'))
        while Self.running:
            msg = Self.body.recv(1024)
            msg = msg.decode("utf-8")
            print (msg)
            if msg != "\'\'keep alive\'\'":
                Self.last = msg
            Self.body.sendall("\'\'keep alive\'\'".encode('utf-8'))
        
        Self.body.close()


th = MultiService (6001, "localhost")
print ("na")