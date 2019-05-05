#!/usr/bin/python3

import sys
import math
import random
import argparse
import logging
import gzip
from Cache import *

######## constants ##############
cache_line_size = 64
offset_bits = int(math.log(64, 2))
######## user interface #########

parser = argparse.ArgumentParser(description='Cache Simulator.')

parser.add_argument('-s', '--size', metavar='N', type=str, dest='size',
                    help='the size of the cache in B, KB or MB', required=True)

parser.add_argument('-a', '--assoc', dest='assoc', type=int, metavar='s',
                    help='the set associativity of the cache', required=True)

parser.add_argument('-f', '--file', metavar='FILENAME', type=str, dest='file',
                    help="name of the input memory trace file; if the file is "
                    "in gzip format, the file name must end with .gz",
                    required=True)

parser.add_argument('--debug', dest='debug', action='store_const',
                    const=True, default=False,
                    help='enable debugging logs')

parser.add_argument('--print', dest='enable_print', action='store_const',
                    const=True, default=False,
                    help='enable cache content output')

args = parser.parse_args()

if args.debug:
    logging.basicConfig(level=logging.DEBUG)

######## helper functions ########
# parse the user-input size string, returns the size in bytes

def parse_size(size):
    try:
        if size.endswith('KB'): 
            s = int(size[:-2]) * 1024
        elif size.endswith('MB'):
            s = int(size[:-2]) * 1024 * 1024
        elif size.endswith('B'):
            s = int(size[:-1])
        else: # just the integer
            s = int(size)
    except ValueError:
        print("Invalid cache size")
        sys.exit(1)
    return s

traceFile = open (args.file, "r")

hit = 0
miss = 0
total = 0

cache = Cache(parse_size(args.size),args.assoc,cache_line_size)

for line in traceFile:
    words = line.split(" ")
    # This will skip blank lines and EOFs
    if len(words) == 3:
        accessMode = words[1].upper()
        virtAddrss = int(words[2],16)
        result = cache.getAddress(accessMode, virtAddrss)
        if result == 1:
            miss+=1
    total+=1

missRate = miss/total
missPercentage = missRate * 100
print('Cache miss rate: %.2f%%'%missPercentage)