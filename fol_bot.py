from TwitterFollowBot import TwitterBot
import random
import time
config = 'config.txt'

while True:
    my_bot = TwitterBot(config)
    if not os.path.isfile('followers.txt'):
        my_bot.sync_follows()
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
        while True:
            following_bot = my_bot.get_follows_list()
            followers_bot = my_bot.get_followers_list()
            not_following_back_bot = following_bot - followers_bot
            not_following_back_bot = list(not_following_back_bot)

            if len(not_following_back_bot) < 700:

                print('%sPhase of follow 1%s' % (stars, stars))
                print(time.asctime(), '\n')
                my_bot.auto_follow_followers_of_user('vasial9', count = random.randint(70, 110))

                print('%sWaiting%s' % (stars, stars))
                random.seed() # N0onsense  99.4
                time.sleep(random.randint(9*60*60, 12*60*60))

                print('%sPhase of follow 2%s' % (stars, stars))
                my_bot.auto_follow_followers_of_user('vasial9', count = random.randint(70, 110))

                print('%sWaiting%s' % (stars, stars))
                time.sleep(random.randint(5*60*60, 6*60*60))

                print('%sPhase of follow followers%s' % (stars, stars))
                my_bot.sync_follows()
                my_bot.auto_follow_followers()

                print('%sWaiting%s' % (stars, stars))
                time.sleep(random.randint(3*60*60, 4*60*60))

            else:
                print('%sWaiting 2 days%s' % (stars, stars))
                print(time.asctime(), '\n')
                time.sleep(random.randint(23*60*60, 26*60*60))

                my_bot.sync_follows()
                my_bot.auto_follow_followers()

                time.sleep(random.randint(23*60*60, 24*60*60))

                print('%sPhase of unfollow nonfollowers%s' % (stars, stars))
                print(time.asctime(), '\n')

                my_bot.sync_follows()
                non_unfollow = []
                with open('non_followers.txt', "r") as in_file:
                    for line in in_file:
                        non_unfollow.append(int(line))

                with open('followers.txt', "a") as out_file:
                    for follower in non_unfollow:
                        out_file.write("%s\n" % (follower))

                my_bot.auto_unfollow_nonfollowers()
                print('%sWaiting%s' % (stars, stars))
                time.sleep(random.randint(15*60*60, 20*60*60))
                my_bot.sync_follows()


        if command == 'bf':
            while True:
                random.seed()
                my_bot.sync_follows()
                my_bot.auto_follow_followers()
                time.sleep(random.randint(23.5*60*60, 24.5*60*60))

        if command == 'bfunf':

            random.seed()
            for i in range(2):
                my_bot.sync_follows()
                my_bot.auto_follow_followers()
                time.sleep(random.randint(22*60*60, 24*60*60))

            non_unfollow = []
            with open('non_followers.txt', "r") as in_file:
                for line in in_file:
                    non_unfollow.append(int(line))

            with open('followers.txt', "a") as out_file:
                for follower in non_unfollow:
                    out_file.write("%s\n" % (follower))

            my_bot.auto_unfollow_nonfollowers()

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
