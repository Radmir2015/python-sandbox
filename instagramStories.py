from instagram_private_api import Client, ClientCompatPatch, endpoints
import datetime
import json

user_name = '<put your login here>'
password = '<put your password here>'

def saveJsonFile(filename, content):
	with open(filename, "w") as file:
		file.write(json.dumps(content, indent=4))

def saveFile(filename, content):
	with open(filename, "w") as file:
		file.write(content)

def getStories(user_id, needSave=False):
	users = []
	for s in user_id:
		user = []
		data = api.user_story_feed(s[1])["reel"]["items"]
		# saveJsonFile("data.json", data)
		if len(data) <= 1:
			user.append([s[0], data[0]["id"], data[0]["taken_at"]])
		else:
			for item in data:
				user.append([s[0], item["id"], item["taken_at"]])
		users.append(user)
	if needSave:
		total = []
		for user in users:
			for story in user:
				total.append(story)
		# saveFile("stories.txt", "\n".join(list(", ".join(map(str, k) for k in u) for u in users)))
		saveFile("stories.txt", "\n".join(" ".join(map(str, t)) for t in total))
	return users

def idFromMediaId(media_id):
	return media_id[media_id.index("_") + 1:]

def seeStories(users): # [[["username", "media_id+id", "timestamp"], ["username", ...]]]
	usernames = []
	total = {}
	for user in users:
		usernames.append(user[0][0])
		for story in user:
			id = idFromMediaId(story[1])
			total["{}_{}".format(story[1], id)] = ["{}_{}".format(story[2], int(story[2]) + 10)]
	# print(total)
	print("I watch the stories of these people: {}".format(", ".join(usernames)))
	# api.media_seen(total)

now = datetime.datetime.now()

# api = Client(user_name, password, proxy="https://45.32.146.119:3128")
api = Client(user_name, password)

user_id = list([item["user"]["username"], item["user"]["pk"]] for item in api.reels_tray()["tray"])

print(len(user_id), user_id)

stories = getStories(user_id, True)

seeStories(stories[:3])

print("Totally spent time: " + str(datetime.datetime.now() - now))