import json
h = list('0123456789abcdef')
k = {}
key = list(",<.>/?;:]}{[|+=(")
for i in range(99):
    k[i] = key[int(99/(i+1))]

with open('dump.txt', 'w') as f:
    json.dump(k,f)