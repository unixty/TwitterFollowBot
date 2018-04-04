from TwitterFollowBot import TwitterBot
import random
import time
import os

config = 'config.txt'
my_bot = TwitterBot(config)

stars = '*' * 10

if not os.path.isfile('followers.txt'):
    print('%sPhase of follow followers%s' % (stars, stars))
    print(time.asctime(), '\n')
    my_bot.sync_follows()
    my_bot.auto_follow_followers()

    print('%sWaiting 6-7h%s' % (stars, stars))
    print(time.asctime(), '\n')
    time.sleep(random.randint(6*60*60, 7*60*60))

while True:
    following_bot = my_bot.get_follows_list()
    followers_bot = my_bot.get_followers_list()
    not_following_back_bot = following_bot - followers_bot
    not_following_back_bot = list(not_following_back_bot)

    if len(not_following_back_bot) < 900:

        print('%sPhase of follow #1%s' % (stars, stars))
        print(time.asctime(), '\n') #_FireAnt - 100% audit, vasial9 99.5
        my_bot.auto_follow_followers_of_user('_FireAnt', count = random.randint(180, 210))

        print('%sWaiting 8.5-10.5h%s' % (stars, stars))
        print(time.asctime(), '\n')
        random.seed()
        time.sleep(random.randint(8.5*60*60, 10.5*60*60))

        print('%sPhase of follow #2%s' % (stars, stars))
        print(time.asctime(), '\n')
        my_bot.auto_follow_followers_of_user('_FireAnt', count = random.randint(180, 210))

        print('%sWaiting 5-6h%s' % (stars, stars))
        print(time.asctime(), '\n')
        time.sleep(random.randint(5*60*60, 6*60*60))

        print('%sPhase of follow followers%s' % (stars, stars))
        print(time.asctime(), '\n')
        my_bot.sync_follows()
        my_bot.auto_follow_followers()


        print('%sWaiting 3-4h%s' % (stars, stars))
        print(time.asctime(), '\n')
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
        print('%sWaiting 17h%s' % (stars, stars))
        time.sleep(random.randint(15*60*60, 20*60*60))
        my_bot.sync_follows()
