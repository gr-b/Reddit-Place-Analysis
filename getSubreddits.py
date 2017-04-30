import json, praw

def getSub(rawname):
    subname = ''
    hasHitText = False
    for char in rawname:
        if not hasHitText:
            if char == 'r':
                hasHitText = True
                subname += char
        elif hasHitText:
            #if char == '/':
             #   return subname
            subname += char
    if subname[:2] == 'r/':
        subname = subname[2:]
    if len(subname) > 0 and subname[-1] == '/':
        subname = subname[:-1]
    return subname

infile = open('areas2.json','r')

items = []
for line in infile:
    item = json.loads(line)
    items += [item]


reddit = praw.Reddit(user_agent='DS3001 Group 3',
                     client_id='G24ch0kTE7WWdg',
                     client_secret="OpT4JxILDWB5YoTbmeHPccZneis",
                     username='SeventhSectionSword',
                     password='jscripter1')

outfile = open('subscribers2.json','w')

for item in items:
    subname = getSub(item['sub'])
    print subname
    if subname == '':
        continue
    if subname == 'rffortress':
        subname = 'dwarffortress'
    try:
        item['subscribers']= reddit.subreddit(subname).subscribers
    except:
        pass
    item['sub'] = subname
    outfile.write(json.dumps(item)+'\n')
