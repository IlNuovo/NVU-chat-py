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

    def save_conf (Self, data, path : str):
        name = path.strip()
        with open(name,"w") as nwFile:
            json.dump(data, nwFile)
    
    def extract_conf (Self, path : str):
        name = path.strip()
        res = None
        with open(name,"r") as nwFile:
            res = json.load(nwFile)
        return res

#example:
#
config = configurator()
#config.create_conf("./conf.json")
extr = config.extract_conf("./conf.json")
extr["track"] = False
config.save_conf(extr, "./conf.json")