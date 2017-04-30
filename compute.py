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
ratios = []
for item in sorted_items:
    #print "{} : {}".format(item['sub'], item['ratio'])
    if item['ratio'] < 100:
        ratios += [item['ratio']]

import matplotlib.pyplot as plt
num = len(ratios)
plt.hist(ratios, bins=20)
plt.title('Histogram of subscriber-pixels controlled ratios in ' + str(num) + ' subreddits')
plt.ylabel('Frequency')
plt.xlabel('Ratio (Removed above 500)')
plt.show()

