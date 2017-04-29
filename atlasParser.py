import json

infile = open('atlas.js','r')
outfile = open('parsedatlas.json','w')

inobject = False

for line in infile:
    for char in line:
        if not inobject:
            if char == '{':
                inobject = True
                outfile.write(char)
        elif inobject:
            if char == '}':
                inobject = False
                outfile.write(char + '\n')
            elif char != '\n':
                outfile.write(char)
print 'done'
            
        
