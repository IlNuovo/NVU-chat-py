from threading import Thread
import socket
from time import sleep
from Builder import Structurer



class MultiService:
    def __init__ (Self, s_port : int, srv : str, link):
        Self.sender = Port(ip_bind=srv, port=s_port, link=link)
        if Self.sender == -1:
            return None
        pass
    def send_msg (Self, message):
        Self.sender.addSend(message)



class Port (Thread):
    def __init__(Self, group = None, target = None, name = None, args = ..., kwargs = None, *, daemon = None, ip_bind = "0.0.0.0", port : int, link):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        Self.body = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Self.ip_bind = ip_bind
        Self.port = port
        Self.running = True
        Self.send = []
        Self.recv_log = []
        Self.link = link
        Self.start()

    def run (Self):
        host = socket.gethostbyname(socket.gethostname())
        builder = Structurer()
        try:
            Self.body.connect((Self.ip_bind, Self.port))
        except:
            print('connection failed')
            return -1
        print (f"added {Self.body}")
        sleep(1)
        Self.body.sendall(builder.build(ip=host, message=builder.key, keepalive=True, encripted=False, encoding='utf-8'))
        while Self.running:
            msg = Self.body.recv(1024)
            msg = msg.decode("utf-8")
            received = builder.unpack(msg,encripted=False)

            if not(received['message'].strip() == ''):
                print ('message: ', received["message"])
                Self.recv_log.append(received["message"])
                Self.link(received["message"])
            
            tmp = builder.build(ip=host,encripted=False, message=Self.getSend())
            Self.body.sendall(tmp)

            if not (received['keepalive']) or msg == b'':
                Self.running = False
        Self.body.sendall(builder.build(ip=host,keepalive=False))
        Self.body.close()
    def addSend (Self, added):
        Self.send.append(added)
    def getSend(Self) -> str:
        if len(Self.send) > 0:
            return Self.send.pop(0)
        else:
            return ""


#failure = True
#port = 6000
#while failure:
#    try:
#        print(f'connecting to server on port {port}')
#        th = MultiService (port, "localhost")
#        failure = False
#    except:
#        print(f'increased port to {port}')
#        failure = True
#        port += 1
#print ("na")


#th = MultiService (6002, "localhost")
#th.send_msg(input())
#th.send_msg(input())
#th.sender.running = False