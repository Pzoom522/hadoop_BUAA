#!/usr/bin/python
import sys
import json
order_list = {}
line_item = {}
for line in sys.stdin:
    line = line.strip()
    Id, words = line.split('\t')
    record = json.loads(words)
    if int(Id) > 100:
        order_list[int(Id)-100] = record
    else:
        for List in order_list:
            if int(Id) == List:
                ans = []
                for word in order_list[List]:
                    ans.append(word)
                for word in record:
                    ans.append(word)
                ans = json.dumps(ans)
                print ans
