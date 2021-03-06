#!/usr/bin/env python3

"""Revamped collatz code from Prof. Downing's CS 373 project"""

import copy
from .common import main

# Local maxima of max-cycle-length from 1 to 1,000,000
local_maxima = {
    1: 1,
    2: 2,
    3: 8,
    6: 9,
    7: 17,
    9: 20,
    18: 21,
    19: 21,
    25: 24,
    27: 112,
    54: 113,
    55: 113,
    73: 116,
    97: 119,
    129: 122,
    171: 125,
    231: 128,
    235: 128,
    313: 131,
    327: 144,
    649: 145,
    654: 145,
    655: 145,
    667: 145,
    703: 171,
    871: 179,
    1161: 182,
    2223: 183,
    2322: 183,
    2323: 183,
    2463: 209,
    2919: 217,
    3711: 238,
    6171: 262,
    10971: 268,
    13255: 276,
    17647: 279,
    17673: 279,
    23529: 282,
    26623: 308,
    34239: 311,
    35497: 311,
    35655: 324,
    52527: 340,
    77031: 351,
    106239: 354,
    142587: 375,
    156159: 383,
    216367: 386,
    230631: 443,
    410011: 449,
    511935: 470,
    626331: 509,
    837799: 525
}

# Populating the cache with local maxima from 837,800 to 1,000,000
post_local_maxima = {
    837800: 145,
    837801: 189,
    837807: 282,
    838447: 282,
    838591: 313,
    838683: 344,
    839547: 388,
    842881: 388,
    845223: 401,
    847358: 419,
    847359: 419,
    854191: 419,
    871915: 432,
    875681: 432,
    886953: 445,
    906175: 445,
    910107: 476,
    927003: 476,
    939497: 507,
    939498: 109,
    939499: 171,
    939528: 202,
    939530: 202,
    939532: 202,
    939533: 202,
    939537: 202,
    939548: 202,
    939549: 202,
    939550: 202,
    939552: 202,
    939560: 202,
    939562: 202,
    939568: 202,
    939572: 202,
    939573: 202,
    939584: 202,
    939588: 202,
    939589: 202,
    939590: 202,
    939592: 202,
    939594: 202,
    939595: 202,
    939596: 202,
    939597: 202,
    939600: 202,
    939604: 202,
    939605: 202,
    939616: 202,
    939617: 202,
    939624: 202,
    939626: 202,
    939633: 202,
    939650: 202,
    939651: 202,
    939673: 277,
    939675: 277,
    939729: 277,
    939730: 277,
    939731: 277,
    939772: 277,
    939773: 277,
    939774: 277,
    939794: 308,
    939795: 308,
    939803: 308,
    940088: 308,
    940090: 308,
    940092: 308,
    940093: 308,
    940097: 308,
    940098: 308,
    940099: 308,
    940104: 308,
    940106: 308,
    940108: 308,
    940109: 308,
    940113: 308,
    940114: 308,
    940115: 308,
    940140: 308,
    940141: 308,
    940142: 308,
    940153: 308,
    940207: 308,
    940257: 383,
    944491: 383,
    946623: 383,
    947049: 383,
    948242: 383,
    948243: 383,
    950943: 414,
    952479: 414,
    953279: 414,
    960962: 414,
    960963: 414,
    963113: 414,
    970599: 458
}

# Populating the cache
meta_cache = copy.deepcopy(local_maxima)
meta_cache.update(post_local_maxima)

def collatz_eval(i, j):
    """Return the max cycle length of the range [i, j]"""
    max_cycle_len = 0
    if i == j:
        return collatz_cycle(i)
    if i > j:
        i, j = (j, i)
    midpoint = j // 2 + 1
    if i < midpoint:
        i = midpoint
    for k in range(j, i + 1, -1):
        if k in local_maxima:
            return local_maxima[k]
    for value in range(i, j + 1):
        assert value > 0
        if value in meta_cache:
            cycle_len = meta_cache[value]
        else:
            cycle_len = collatz_cycle(value)
            meta_cache[value] = cycle_len
        if cycle_len > max_cycle_len:
            max_cycle_len = cycle_len
        assert cycle_len > 0
    assert max_cycle_len > 0
    return max_cycle_len

def collatz_cycle(value):
    """Recursively compute the collatz cycle length"""
    if value in meta_cache:
        return meta_cache[value]
    if (value % 2) == 0:
        return collatz_cycle(value // 2) + 1
    return collatz_cycle(value + (value >> 1) + 1) + 2

if __name__ == "__main__": # pragma: no cover
    main(collatz_eval, int, "Beginning of range", "End of range")
