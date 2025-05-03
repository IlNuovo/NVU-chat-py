from cryptography.fernet import Fernet


class Structurer:

    def __init__(Self):
        Self.key = Fernet.generate_key()
        Self.cipher_suite = Fernet(Self.key)

    def build (Self, ip = 'localhost', message = '', keepalive = True, encripted = True, encoding = 'utf-8'):
        final = ""

        final += f"from : {ip}-"
        final += f"msg : {message}-"
        final += f"keepalive : {keepalive}"

        if encripted:
            final = Self.cipher_suite.encrypt(final.encode(encoding))
        
        return final
    
    def unpack (Self, cipher_text, encoding = 'utf-8', encripted = True):
        if encripted:
            plain_text = Self.cipher_suite.decrypt(cipher_text).decode(encoding)
        else:
            plain_text = cipher_text
        #the first information is the sender
        sender = plain_text[0 : plain_text.find('-')]
        nextstep = plain_text[plain_text.find('msg : '):]
        
        #then i find and extract the message
        msg = nextstep[0 : nextstep.find('-')]
        nextstep = plain_text[plain_text.find('keepalive : '):]

        print(nextstep)
        keepalive = False
        if not(nextstep.find('True') == -1):
            keepalive = True
        else:
            keepalive = False

        return {
            'sender' : sender[sender.find(':')+1:],
            'message' : msg[msg.find(':')+1:],
            'keepalive' : keepalive
        }
    
    def setKey (Self, key):
        Self.key = key
        Self.cipher_suite = Fernet(Self.key)


builder = Structurer()

print()
print(builder.unpack(builder.build(message='ciao')))
