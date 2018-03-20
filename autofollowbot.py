from TwitterFollowBot import TwitterBot
import random
import time
config = 'config.txt'

while True:
    my_bot = TwitterBot(config)
    stars = '*' * 15
    print(
'''
         %s TwitterFollowBot %s
    c - change config(%s), af - autofollow followers,
    unf - unfollow nonfollowers, afp - autofollow follower of user,
    afh - hashtag following, b - bot, sf - sync follows, bf - bot autofollow
    followers, e - exit
    ''' % (stars, stars, config)
    )

    command = input('>>>')

    if command == 'sf':
        my_bot.sync_follows()

    if command == 'af':
        my_bot.auto_follow_followers()

    if command == 'c':
        config = input('Input name of config file: ')
        my_bot.sync_follows()

    if command == 'afh':
        my_bot.auto_follow("#FollowBack #Bounty", count=1000)

    if command == 'b':
        if not os.path.isfile('followers.txt'):
            my_bot.sync_follows()

        while True:
            print('Starting bot%s' % (stars))
            print(time.asctime())

            random.seed() # N0onsense  99.4
            my_bot.auto_follow_followers_of_user('vasial9', count = random.randint(90, 130))
            time.sleep(random.randint(7*60*60, 9*60*60))

            my_bot.sync_follows()
            my_bot.auto_follow_followers_of_user('vasial9', count = random.randint(90, 130))
            time.sleep(random.randint(5*60*60, 6*60*60))

            my_bot.sync_follows()
            my_bot.auto_follow_followers()
            time.sleep(random.randint(3*60*60, 4*60*60))

            following_bot = my_bot.get_follows_list()
            followers_bot = my_bot.get_followers_list()
            not_following_back_bot = following_bot - followers_bot
            not_following_back_bot = list(not_following_back_bot)

            if len(not_following_back_bot) >= 700:
                print('Waiting 2 days%s' % (stars))
                print(time.asctime())

                time.sleep(random.randint(22*60*60, 27*60*60))

                my_bot.sync_follows()
                my_bot.auto_follow_followers()

                time.sleep(random.randint(22*60*60, 27*60*60))

                print('Starting unfollow%s' % (stars))
                my_bot.sync_follows()

                non_unfollow = []
                with open('non_followers.txt', "r") as in_file:
                    for line in in_file:
                        non_unfollow.append(int(line))

                with open('followers.txt', "a") as out_file:
                    for follower in non_unfollow:
                        out_file.write("%s\n" % (follower))

                my_bot.auto_unfollow_nonfollowers()
                time.sleep(random.randint(6*60*60, 9*60*60))
                my_bot.sync_follows()

    if command == 'bf':
        while True:
            random.seed()
            my_bot.sync_follows()
            my_bot.auto_follow_followers()
            time.sleep(random.randint(20*60*60, 25*60*60))

    if command == 'unf':
        non_unfollow = []
        with open('non_followers.txt', "r") as in_file:
            for line in in_file:
                non_unfollow.append(int(line))

        with open('followers.txt', "a") as out_file:
            for follower in non_unfollow:
                out_file.write("%s\n" % (follower))

        my_bot.auto_unfollow_nonfollowers()

    if command == 'e':
        break
