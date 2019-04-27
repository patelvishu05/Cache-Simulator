#!/usr/bin/python3
from collections import defaultdict
from TableEntry import *
import math

class Cache:

    def __init__(self, cacheSize, ways, cacheLineSize):
        self.cacheSize = cacheSize
        self.ways = ways
        self.cacheLineSize = cacheLineSize
        
        self.numberSets = (cacheSize / cacheLineSize) / ways
        self.entries = self.numberSets * ways
        self.entries_per_set = self.entries / self.numberSets

        self.bitSet = math.log(self.numberSets, 2)
        self.bitData = math.log(cacheLineSize, 2)
        self.shiftAmount = self.bitSet + self.bitData

        self.cache = [defaultdict(int) for sets in range(int(self.numberSets))]

    def access(self, mode, address):
        currentAddress = int(address, 16)
        tag = currentAddress >> int (self.shiftAmount)
        setId = ((currentAddress - (tag << int(self.shiftAmount))) >> int(self.bitData))
        entry = TableEntry (setId, tag, 1)

        if entry.tag not in self.cache[setId].keys():
            if len(self.cache[setId]) == self.entries_per_set:
                oldest_tag = max(self.lru_cache[setId], key=lambda time_stamp: self.lru_cache[set_id][time_stamp])
                del (self.cache[setId][oldest_tag])
                self.cache[setId].__setitem__(entry.tag, entry.timeStamp)
            else:
                self.cache[setId].__setitem__(entry.tag, entry.timeStamp)
            self.increment_time_stamp(entry, setId)
            return False
        else:
            self.cache[setId].__setitem__(entry.tag, 0)
            self.increment_time_stamp(entry, setId)
            return True

    def increment_time_stamp(self, entry, setId):
        for entry.tag in self.cache[setId]:
            self.cache[setId][entry.tag] += 1