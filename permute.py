import sys
from itertools import *
import time
start_time = time.time()

N = int(sys.argv[1])
num = "0"*N
for x in range(1, N+1):
    num += str(x)
for n in permutations(num):
    print(*n)
print(f"--- {time.time() - start_time} seconds ---")
