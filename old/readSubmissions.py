import json

submissionFile = open('submissions.json','r')

submissions = []

for line in submissionFile:
    submission = json.loads(line)
    new_submission = {'name':submission['name'],
                      'subreddit':submission['subreddit'],
                      'center':submission['center'],
                      'path':submission['path']}
    submissions += [new_submission]

print submissions[0]
