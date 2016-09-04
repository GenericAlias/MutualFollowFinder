from __future__ import print_function
import pprint
import twitter
import sys

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

# Create an Api instance.
api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)

screen_names = sys.argv[1:]

friend_dict = {}
print("Users:")
pprint.pprint(screen_names)
print("\nMutual following:")
# Keep track of follows in common with a map
for name in screen_names:
	users = api.GetFriends(screen_name=name)
	for user in users:
		if user.screen_name not in friend_dict:
			friend_dict[user.screen_name] = 1
		else:
			friend_dict[user.screen_name] += 1

mutual_friends = []
# If the number of followers is equal to the arguments, add it to
# the final result
for key in friend_dict:
	if friend_dict[key] == len(screen_names):
		mutual_friends.append(key)

pprint.pprint([u for u in mutual_friends])