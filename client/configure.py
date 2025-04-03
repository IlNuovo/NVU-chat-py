import json
import uuid

class configurator:
    
    DEFAULT_CONFIGURATION = {
        "server" : "0.0.0.0",
        "MAC": hex(uuid.getnode()),
        "track" : False
    }

    def __init__ (Self):
        pass


    def create_conf (Self, path : str):
        name = path.strip()
        with open(name,"w") as nwFile:
            json.dump(Self.DEFAULT_CONFIGURATION, nwFile)

#example:
#
config = configurator()
config.create_conf("client/conf.json")