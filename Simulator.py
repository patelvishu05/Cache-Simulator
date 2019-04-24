#!/usr/bin/python3

import sys
import math
import random

traceFile = open (sys.argv[1], "r")

for line in traceFile:
    words = line.split(" ")
    accessMode = words[1]
    virtAddrss = words[2]
    break