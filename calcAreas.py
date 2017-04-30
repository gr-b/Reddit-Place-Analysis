import json
import math
infile = open('parsedatlas.json','r')

num= 0
goodsubs = []
for line in infile:
    try:
        sub = json.loads(line)
        num += 1
        goodsubs += [sub]
    except:
        pass
        #print 'Error'
    #print sub['name']

items = []
for sub in goodsubs:
    # Calculate the area of the polygon
    if sub['subreddit'] == '':
        continue
    elif len(sub['subreddit'].split(',')) > 1:
        sub['subreddit'] = sub['subreddit'].split(',')[0]
    subreddit = sub['subreddit']
    points = sub['path']

    total1 = 0
    total2 = 0
    for i in range(len(points)-1):
        total1 += points[i][0] * points[i+1][1]
    for i in range(len(points)-1):
        total2 += points[i][1] * points[i+1][0]

    total = total2 - total1
    total = math.fabs(total/2)

    #print("{} : {}".format(subreddit, total))
    #sub['subreddit'] = sub['subreddit'].split('/')[len(sub['subreddit'].split('/'))-1]
    item = {'sub':sub['subreddit'], 'area':total, 'path':points}
    items += [item]
    #print point

outfile = open('areas2.json','w')
for item in items:
    outfile.write(json.dumps(item) + '\n')
        
        
    
