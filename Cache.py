#!/usr/bin/python3
import math
from WriteBack import *

class Cache:

    def __init__(self, cacheSize, ways, cacheLineSize, hitCost=0):
        self.cacheSize = cacheSize
        self.ways = ways
        self.cacheLineSize = cacheLineSize
        self.hitCost = hitCost
        self.writeBack = WriteBack()
        self.numberSets = int((cacheSize / cacheLineSize) / ways)
        self.writeBack.cache = self
        self.sets = [CacheSet(ways) for i in range(self.numberSets)]
        self.bitSet = math.log(self.numberSets, 2)
        self.bitData = math.log(cacheLineSize, 2)
        self.shiftAmount = int(self.bitSet + self.bitData)

    def getAddress(self,mode,address):

        if type(address) == tuple:
            tag,setId,offset = address
        else:
            offset = address & (self.cacheLineSize - 1)
            setId = address >> int(math.log(self.cacheLineSize, 2)) & (self.numberSets - 1)
            tag = address >> self.shiftAmount


        if mode == 'W':
            return self.hitCost + self.writeBack.write((tag,setId,offset))

        if mode == 'R':
            currentSet = self.sets[setId]
            
            if currentSet.read(tag):
                return self.hitCost
            else:
                index = self.LRU(currentSet)

                removed = currentSet.ways[index]
                removed['valid'] = 1
                removed['tag'] = tag
                removed['last_access'] = currentSet.timeStamp

                return 1 + self.hitCost

    def LRU(self,cache):
        for i, cacheLine in enumerate(cache.ways):
            if not cacheLine["valid"]:
                return i
                
        leastPolicy = cache.ways[0]
        index = 0
        for i, cacheLine in enumerate(cache.ways[1:]):
            if leastPolicy["last_access"] > cacheLine["last_access"]:
                leastPolicy = cacheLine
                index = i+1
        return index


class CacheSet:

    def __init__(self, ways):
        self.ways = [
            {
                'tag': None,
                'valid': 0,
                'last_access': 0,
            } for i in range(ways)
        ]
        self.timeStamp = 0

    def read(self, tag):
        self.timeStamp += 1

        for way in self.ways:
            if tag == way['tag']:
                way['last_access'] = self.timeStamp
                return True
        return False

    def write(self, tag):
        self.timeStamp += 1               

    