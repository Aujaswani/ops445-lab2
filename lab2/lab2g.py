#!/usr/bin/env python3
import sys

if len(sys.argv) == 2:
 count = int(sys.argv[1])

else: count = 3



while count > 0:
 print(str(count))
 count = count - 1
 
print("blast off!")