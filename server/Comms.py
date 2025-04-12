from threading import Thread
import socket



class MultiService (Thread):
    def __init__ (Self, start : int, end : int, mode : int, network : str):
        super().__init__(None, "gestion", None,None, None)
        if start < end:
            Self.start_port = start
            Self.end_port = end
        else:
            Self.start_port = end
            Self.end_port = start
        Self.mode = mode
        Self.bind_net = network
        Self.ports = []

        
    
    def run (Self):
        for i in range(Self.end_port-Self.start_port):
            print (f"adding port {Self.start_port + i} to ports")
            Self.ports.append(Port(ip_bind=Self.bind_net, port=Self.start_port+i))
        pass
        print (f"service start whith {Self.end_port-Self.start_port} ports")

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
        Self.last = ""
        if Self.listen:
            Self.body.bind((socket.gethostname(), Self.port))
            Self.body.listen()
            client, cl_ip = Self.body.accept()
            print (f"added {Self.body}")
            while Self.running:
                msg = Self.body.recv(1024)
                msg = msg.decode("utf-8")
                print (msg)
                if msg != "":
                    Self.last = msg
            
        
        


trial = MultiService(6000, 6002, 0, "0.0.0.0")



trial.start()
trial.join()


print(0)