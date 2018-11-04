from TwitterFollowBot import TwitterBot
import random
import time
import os

def check_alr_fol():
        followers_a = []
        with open('followers.txt', "r") as followers_txt:
            for  follower in followers_txt:
                followers_a.append(int(follower))
        alr_follow = []
        with open('/home/scripts/twitter/already-followed.txt', "r") as already_txt:
            for non_follower in already_txt:
                alr_follow.append(int(non_follower))
        i = 0
        while i < len(alr_follow):
            if (alr_follow[i] in followers_a):
                del alr_follow[i]
            i += 1

        with open('/home/scripts/twitter/already-followed.txt', "w") as out_file:
            for non_follower in alr_follow:
                out_file.write("%s\n" % (non_follower))

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

    if len(not_following_back_bot) < 400:

        print('%sPhase of follow #1%s' % (stars, stars))
        print(time.asctime(), '\n') #_FireAnt - 100% audit, vasial9 99.5
        my_bot.auto_follow_followers_of_user('alzambek', count = random.randint(20, 40))

        print('%sWaiting 9-12h%s' % (stars, stars))
        print(time.asctime(), '\n')
        random.seed()
        time.sleep(random.randint(9*60*60, 12*60*60))

        print('%sPhase of follow #2%s' % (stars, stars))
        print(time.asctime(), '\n')
        my_bot.auto_follow_followers_of_user('alzambek', count = random.randint(30, 38))

        print('%sWaiting 8-10h%s' % (stars, stars))
        print(time.asctime(), '\n')
        time.sleep(random.randint(8*60*60, 10*60*60))

        print('%sPhase of follow followers%s' % (stars, stars))
        print(time.asctime(), '\n')
        my_bot.sync_follows()
        check_alr_fol()
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
            for following in non_unfollow:
                out_file.write("%s\n" % (following))

        my_bot.auto_unfollow_nonfollowers()

        print('%sWaiting 17h%s' % (stars, stars))
        time.sleep(random.randint(15*60*60, 20*60*60))
        my_bot.sync_follows()
        #check for followers in already_follow
        check_alr_fol()
