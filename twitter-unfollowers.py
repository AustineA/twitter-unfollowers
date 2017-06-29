import twitter, time, json

with open('config.json') as data_file:
    json = json.load(data_file)

api = twitter.Api(consumer_key=json['twitter']['consumer_key'],
                      consumer_secret=json['twitter']['consumer_secret'],
                      access_token_key=json['twitter']['access_token_key'],
                      access_token_secret=json['twitter']['access_token_secret'])

print api.VerifyCredentials()

# Get all followers from users in array
friends = []
for name in json['accounts']:
    sec = api.GetSleepTime('/followers/list') + 2 # Wait 2 seconds more to make sure rate-limit is avoided

    time.sleep(sec)
    print 'Fetching followers for {0}...'.format(name)
    followers = api.GetFollowerIDs(screen_name=name)

    time.sleep(sec)
    print 'Fetching friends for {0}...'.format(name)
    friends = api.GetFriendIDs(screen_name=name)

    following = set(friends) - set(followers)

    usernames = list()
    index = 0
    for user in following:
        time.sleep(sec)
        index += 1
        print 'Fetching screen name for {0} ({1}/{2})'.format(user, index, len(following))
        usernames.append(api.GetUser(user_id=user).screen_name)

    print
    print 'People who are not following back {0}'.format(name)
    print
    for user in usernames:
        print user
    print