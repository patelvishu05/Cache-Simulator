#!/bin/bash

if [[ "$#" -le 0 ]]; then
    echo "Usage: Provide a valid trace after the wrapper script"
else
    python3 Simulator.py -s 1MB -a 16 -f $1
fi

# python3 Simulator.py -s 1KB -a 16 -f 1KB_64B
# python3 Simulator.py -s 4MB -a 16 -f 4MB_4
# python3 Simulator.py -s 4MB -a 16 -f 32MB_4B
# python3 Simulator.py -s 4MB -a 16 -f bw_mem.traces.txt
# python3 Simulator.py -s 32KB -a 16 -f ls.trace.txt
# python3 Simulator.py -s 32KB -a 16 -f gcc.trace.txt
# python3 Simulator.py -s 256KB -a 16 -f naive_dgemm.trace.txt
# python3 Simulator.py -s 256KB -a 16 -f naive_dgemm_full.trace.txt
# python3 Simulator.py -s 256KB -a 16 -f openblas_dgemm.trace.txt


# python3 Simulator.py -s 1KB -a 16 -f 1KB_64B
# python3 Simulator.py -s 1KB -a 1 -f 1KB_64B

# python3 Simulator.py -s 1KB -a 16 -f 4MB_4
# python3 Simulator.py -s 1KB -a 1 -f 4MB_4
# python3 Simulator.py -s 4MB -a 16 -f 4MB_4
# python3 Simulator.py -s 4MB -a 1 -f 4MB_4

# python3 Simulator.py -s 1KB -a 16 -f 32MB_4B
# python3 Simulator.py -s 1KB -a 1 -f 32MB_4B
# python3 Simulator.py -s 32MB -a 16 -f 32MB_4B
# python3 Simulator.py -s 32MB -a 1 -f 32MB_4B