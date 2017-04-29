import praw

outfile = open('submissions.json', 'w')



reddit = praw.Reddit(user_agent='DS3001 Group 3',
                     client_id='G24ch0kTE7WWdg',
                     client_secret="OpT4JxILDWB5YoTbmeHPccZneis",
                     username='SeventhSectionSword',
                     password='jscripter1')
success = 0
total = 0

for submission in reddit.subreddit('placeAtlas').new(limit=10000):
        total += 1
	if(submission.link_flair_text == "New Entry"):
		text = submission.selftext
		#text = text.replace("\"id\": 0,", "\"id\": 0,\n\t\t\"submitted_by\": \""+submission.author.name+"\",")
                text = text.replace("\n","")
		
		
		try:
                    outfile.write((text+"\n").encode('utf-8'))
                    print("written "+submission.title)
                    success += 1
                except:
                    print("Erorr")
	else:
		print("skipped ")

print("Total: {}. Success: {}".format(total, success))
