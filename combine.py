import json

file1 = open('areas2.json','r')
file2 = open('subscribers.json','r')

areas = []
for line in file1:
    areas += [json.loads(line)]

subscribers = []
for line in file2:
    subscribers += [json.loads(line)]

print len(areas), len(subscribers)
combined = []
#for i in range(len(subsc
