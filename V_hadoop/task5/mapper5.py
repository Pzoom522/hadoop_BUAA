#!/usr/bin/python
import sys
import json
for line in sys.stdin:
    line = line.strip()
    record = json.loads(line)
    seqId = record[0]
    nucleotide = record[1]
    trimmedNucleotide = nucleotide[:-10]
    print '%s#%s' % (trimmedNucleotide, seqId)
