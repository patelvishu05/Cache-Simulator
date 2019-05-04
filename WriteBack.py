#!/usr/bin/python3
class WriteBack:
    
    def __init__(self):
        self.cache = None

    def write(self, address):
        tag, setId, offset = address
        for cacheLine in self.cache.sets[setId].ways:
            if tag == cacheLine["tag"]:
                return 0
        return self.cache.getAddress('R',address)