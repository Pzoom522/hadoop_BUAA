#!/usr/bin/python

import sys
result= {}
for line in sys.stdin:
    line = line.strip()
    trimmedNucleotide,seqIds = line.split('#', 1)
    try:
        result[trimmedNucleotide] = 0
    except ValueError:
        pass
for word in result:
	print '%s' % (word)
