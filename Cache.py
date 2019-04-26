#!/usr/bin/python3
from collections imort defaultdict
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
        
