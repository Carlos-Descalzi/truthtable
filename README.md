# truthtable
build and show a truth table from a boolean expression.

Just a piece of old code I had in my hard drive and I wanted to preserve with some reaconditioning.

## Example:
```bash
truthtable "(((a & b) | (a & c)) ^ d) & b"
```
Will produce:
```
a | b | c | d | a & b | a & c | ( a & b ) | ( a & c ) | ( ( a & b ) | ( a & c ) ) ^ d | ( ( ( a & b ) | ( a & c ) ) ^ d ) & b
-----------------------------------------------------------------------------------------------------------------------------
0 | 0 | 0 | 0 |     0 |     0 |                     0 |                             0 |                                     0
0 | 0 | 0 | 1 |     0 |     0 |                     0 |                             1 |                                     0
0 | 0 | 1 | 0 |     0 |     0 |                     0 |                             0 |                                     0
0 | 0 | 1 | 1 |     0 |     0 |                     0 |                             1 |                                     0
0 | 1 | 0 | 0 |     0 |     0 |                     0 |                             0 |                                     0
0 | 1 | 0 | 1 |     0 |     0 |                     0 |                             1 |                                     1
0 | 1 | 1 | 0 |     0 |     0 |                     0 |                             0 |                                     0
0 | 1 | 1 | 1 |     0 |     0 |                     0 |                             1 |                                     1
1 | 0 | 0 | 0 |     0 |     0 |                     0 |                             0 |                                     0
1 | 0 | 0 | 1 |     0 |     0 |                     0 |                             1 |                                     0
1 | 0 | 1 | 0 |     0 |     1 |                     1 |                             1 |                                     0
1 | 0 | 1 | 1 |     0 |     1 |                     1 |                             0 |                                     0
1 | 1 | 0 | 0 |     1 |     0 |                     1 |                             1 |                                     1
1 | 1 | 0 | 1 |     1 |     0 |                     1 |                             0 |                                     0
1 | 1 | 1 | 0 |     1 |     1 |                     1 |                             1 |                                     1
1 | 1 | 1 | 1 |     1 |     1 |                     1 |                             0 |                                     0
```
Operators:
- &: and
- |: or
- ^: xor
- ~: not

## Setup
```bash
python3 setup.py install [--prefix=base folder]
```

