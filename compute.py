import json

infile = open('subscribers.json','r')


print '======================================================='
items = []
for line in infile:
    item = json.loads(line)
    #print item
    try:
        item['ratio'] = item['subscribers'] / item['area']
    except:
        continue
    if item['subscribers'] > 1000:
        items += [item]

sorted_items = sorted(items, key= lambda x: x['ratio'])
for item in sorted_items:
    print "{} : {}".format(item['sub'], item['ratio'])
