#!/usr/bin/env python3
"""Check the corrected paper's probability arithmetic and counter bound.

These checks validate the conditional model, not historical Centera behavior.
Only Python's standard library is required.
"""
from fractions import Fraction
from itertools import product
from math import ceil, comb, expm1, isclose, log, prod, sqrt
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def exact_birthday(n, q):
    return 1 - prod((Fraction(n-i, n) for i in range(q)), start=Fraction(1))

# Exhaustive small spaces: exact probability respects the union bound,
# increases with sample count, and reaches one after exhausting the space.
for n in range(2, 65):
    previous = Fraction(0)
    for q in range(n+2):
        p = exact_birthday(n, q)
        assert previous <= p <= min(1, Fraction(q*(q-1), 2*n))
        previous = p
    assert previous == 1
assert exact_birthday(365, 22) < Fraction(1, 2) < exact_birthday(365, 23)
assert (Fraction(364, 365)**252) > Fraction(1, 2)
assert (Fraction(364, 365)**253) < Fraction(1, 2)
assert isclose(-expm1(-0.5), 0.3934693402873666)
assert isclose(sqrt(2*log(2)), 1.1774100225154747)

# Enumerate actual sequential counter writes with arbitrary initial offsets.
# Test quantization at zero, just below/at/above a counter wrap, and beyond.
for c0 in range(2, 9):
    for nodes in range(1, 4):
        for m in [0, 1, c0-1, c0, c0+1, 2*c0+1]:
            bound = nodes * ((m+c0-1)//c0)
            for offsets in product(range(c0), repeat=nodes):
                counts = [0]*c0
                for start in offsets:
                    for k in range(m):
                        counts[(start+k) % c0] += 1
                assert max(counts) <= bound
                assert sum(comb(v, 2) for v in counts) <= c0*comb(bound, 2)

z = 1000*365*24*3600*1000
q = 10000*z//1000
m_probability = q*(q-1)/2**129
mpp_probability = q*(q-1)/2**249
l = (z+1023)//1024 + 1
b = 100 * ((10240+1023)//1024)
gm_bound = l*1024*b*(b-1)/2**199
assert l == 30796875001 and b == 1000
assert isclose(gm_bound, 3.9210552159838466e-41)
assert isclose(m_probability, 1.4613147677896934e-10)
assert isclose(mpp_probability, 1.0993710427583791e-46)

# Check every displayed Table 1 row against recomputed values.
table = (ROOT/'fig/collision-table.tex').read_text()
for power in range(6, 16):
    qrow = 10**power
    p = qrow*(qrow-1)/2**129
    expected = '1.47\\times10^{%d}' % (2*power-39)
    assert expected in table
    assert isclose(p, 1.47*10**(2*power-39), rel_tol=0.001)
    assert qrow*10 == 10**(power+1)
    assert qrow*1000 == 10**(power+3)

# MD5 padding adds one marker bit, zeroes, and a 64-bit length field.
for byte_count in [100_000_000, 100*2**20]:
    padded_blocks = (byte_count*8+1+64+511)//512
    assert padded_blocks < 2**21

# RFC 1321 register integers reproduce its little-endian byte strings.
for value, raw in [(0x67452301,'01234567'),(0xefcdab89,'89abcdef'),
                   (0x98badcfe,'fedcba98'),(0x10325476,'76543210')]:
    assert value.to_bytes(4, 'little').hex() == raw

print(json.dumps({'result':'pass', 'years_of_365_days':1000,
    'files_at_10000_per_second':q, 'M_probability':m_probability,
    'Mpp_probability':mpp_probability, 'GM_upper_bound':gm_bound,
    'GM_timestamp_bins':l, 'GM_max_bin_occupancy':b,
    'birthday_probability_at_sqrt_N':-expm1(-0.5),
    'birthday_50_percent_factor':sqrt(2*log(2))}, indent=2))
