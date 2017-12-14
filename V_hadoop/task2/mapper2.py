#!/usr/bin/python
import sys
import json

for line in sys.stdin:
    line = line.strip()
    record = json.loads(line)
    words = []
    Type = record[0]
    Id = int(record[1])
    for word in record:
        words.append(word)
    if Type == 'order':
        Id = 100 + Id
    print '%s\t%s' % (Id, json.dumps(words))
