from threading import Thread
import socket
from Builder import Structurer





class MultiService (Thread):
    def __init__ (Self, start : int, end : int, network : str, mode = 0, localhost = False):
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
        Self.localhost = localhost
        Self.run()
    
    def reply (Self, message : str, excluded : int):
        for i in Self.ports:
            if not (i.port == excluded):
                i.addSend('message')

        
    
    def run (Self):
        for i in range(Self.end_port-Self.start_port):
            print (f"adding port {Self.start_port + i} to ports")
            Self.ports.append(Port(ip_bind=Self.bind_net, port=Self.start_port+i, localhost=Self.localhost, father=Self))
        pass
        print (f"service start whith {Self.end_port-Self.start_port} ports")

class Port (Thread):
    def __init__(Self, group = None, target = None, name = None, args = ..., kwargs = None, *, daemon = None, listen = True,localhost = False, ip_bind = "0.0.0.0", port : int, father):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        Self.body = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Self.ip_bind = ip_bind
        Self.listen = listen
        Self.port = port
        Self.running = True
        Self.localhost = localhost
        Self.father = father
        Self.send = []
        Self.start()

    def addSend (Self, added):
        Self.send.append(added)
    def getSend(Self) -> str:
        if len(Self.send) > 0:
            return Self.send.pop(0)
        else:
            return ""

    def run (Self):
        builder = Structurer()


        Self.last = ""
        if Self.localhost:
            Self.body.bind(('localhost', Self.port))
        else:
            Self.body.bind((socket.gethostbyname(socket.gethostname()), Self.port))

        #print(f"binded socket at ip {socket.gethostbyname(socket.gethostname())} and port {Self.port}")
        Self.body.listen(10)
        new_comm = True
        client, cl_ip = Self.body.accept()
        print(f"connected to {client} with address {cl_ip}")
        print (f"added {Self.body}")
        while Self.running:
            msg = client.recv(1024)
            if new_comm:
                builder.key = msg
                new_comm = False
            msg = msg.decode("utf-8")
            received = builder.unpack(msg, encripted=False)
            if not(received['message'].strip() == ''):
                Self.father.reply(received['message'], Self.port)
                print('message:',received['message'])
                
            if not(msg == b'') and received['keepalive']:
                client.sendall(builder.build(encripted=False, message=Self.getSend()))
            else:
                new_comm = True
                client, cl_ip = Self.body.accept()
            
            
        
        


trial = MultiService(6000, 6100, "localhost", localhost=True)




