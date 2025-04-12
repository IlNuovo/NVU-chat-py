send = []
recv = []

last_send = None
last_recv = None

def getlastsend ():
    if len(send) > 1:
        return send[-1]
    else:
        return None
def getlastrecv ():
    if len(recv) > 1:
        return recv[-1]
    else:
        return None