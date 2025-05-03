from threading import Thread
import socket



class MultiService (Thread):
    def __init__ (Self, start : int, end : int, network : str, mode = 0):
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
        Self.run()

        
    
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
        #Self.body.bind((socket.gethostbyname(socket.gethostname()), Self.port))
        Self.body.bind(('localhost', Self.port))

        #print(f"binded socket at ip {socket.gethostbyname(socket.gethostname())} and port {Self.port}")
        Self.body.listen(10)
        client, cl_ip = Self.body.accept()
        print(f"connected to {client} with address {cl_ip}")
        print (f"added {Self.body}")
        while Self.running:
            msg = client.recv(1024)
            msg = msg.decode("utf-8")
            print (msg)
            if msg != "":
                Self.last = msg
                
            if not(msg == b''):
                client.sendall("keep alive".encode('utf-8'))
            else:
                break
                Self.body.accept()
                client, cl_ip = Self.body.accept()
            
            
        
        


trial = MultiService(6000, 6100, "localhost")




