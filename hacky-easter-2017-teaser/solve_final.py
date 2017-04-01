#!/usr/bin/env python
import sys
import math
import itertools
import multiprocessing
from multiprocessing.pool import ThreadPool as Pool

import anybase32


# Found flags: (16)
#
# N5XGK
# IDEN4
# ZXGID
# ON52C
# A43JN
# VYGY6
# JAOMY
# GY5TF
# A2DBM
# XIZLS
# EBQSA
# NVXSI
# 5DFME
# ZWK4R
# AGBTC
# DFMFZ

# Pre solved order as the keys were bruteforced partially and populated part by
# part.

L1 = ['N5XGK', 'IDEN4', 'ZXGID', 'ON52C', 'A43JN', 'VYGY6', 'JAOMY', 'GY5TF',
      'EBQSA', '5DFME', 'ZWK4R', 'AGBTC', 'A2DBM', 'NVXSI', 'DFMFZ', 'XIZLS']

def detect_the_thing(combo):
    dec = anybase32.decode(''.join(combo))
    try:
        dec.decode('ascii')
        return combo, dec
    except UnicodeDecodeError:
        pass

total_count = str(math.factorial(len(L1)))
pool = Pool(multiprocessing.cpu_count()*2)

for count, combo in enumerate(pool.imap_unordered(detect_the_thing, itertools.permutations(L1, len(L1)))):
    if combo:
        print combo
    sys.stderr.write(' '.join(('\r'*30, str(count), 'of', total_count, ' ')))
