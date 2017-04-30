import json

infile = open('subscribers2.json','r')

items = []
for line in infile:
    item = json.loads(line)
    #print item
    try:
        item['ratio'] = item['subscribers'] / item['area']
    except:
        continue
    if item['subscribers'] > 8000:
        items += [item]

sorted_items = sorted(items, key= lambda x: x['ratio'])
ratios = []
for item in sorted_items:
    print "{} : {} - > {}".format(item['sub'], item['ratio'], item['area'])
    
    #if item['sub'] == 'wpi' or item['sub'] == 'rpi':
    #    print item
    ratios += [item['ratio']]

'''
from Tkinter import *

master = Tk()
width = 1000
height = 1000
w = Canvas(master, width=width, height=height)
w.pack()

for item in sorted_items:
    arglist = []
    for point in item['path']:
        arglist += point
    if item['area'] < 200000:
        if item['ratio'] > 100:
            color = '#%02x%02x%02x' % (0, 0, 0)
        elif item['ratio'] > 200:
            color = '#%02x%02x%02x' % (25, 0, 0)
        elif item['ratio'] > 100:
            color = '#%02x%02x%02x' % (50, 0, 0)
        elif item['ratio'] > 50:
            color = '#%02x%02x%02x' % (100, 0, 0)
        elif item['ratio'] > 12:
            color = '#%02x%02x%02x' % (150, 0, 0)
        elif item['ratio'] > 3:
            color = '#%02x%02x%02x' % (200, 0, 0)
        else:
            color = '#%02x%02x%02x' % (255, 0, 0)
        w.create_polygon(*arglist, activefill='red', fill=color)

mainloop()
'''
