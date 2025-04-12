from threading import Thread
import socket

class MultiService:
    def __init__ (Self, s_port : int, l_port : int, net = "0.0.0.0"):
        Self.listener = Port(ip_bind=net, port=l_port)
        Self.sender = Port(ip_bind=net, port=s_port, listen=False)
        pass



class Port (Thread):
    def __init__(Self, group = None, target = None, name = None, args = ..., kwargs = None, *, daemon = None, listen = True, ip_bind = "0.0.0.0", port : int):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        Self.body = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Self.ip_bind = ip_bind
        Self.listen = listen
        Self.port = port
        Self.running = True
        Self.start()

    def run (Self):
        if Self.listen:
            Self.body.bind((socket.gethostname(), Self.port))
            Self.body.listen()
            Self.client, Self.cl_ip = Self.body.accept()
            print (f"added {Self.body}")
            while Self.running:
                msg = Self.body.recv(1024)
                msg = msg.decode("utf-8")
                print (msg)
        else:
            pass


th = MultiService (8000, 8001, "0.0.0.0")
print ("na")