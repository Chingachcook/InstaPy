""" Quickstart script for InstaPy usage """
# imports
from instapy import InstaPy
from instapy.util import smart_run

# login credentials
insta_username = 'aliamabay'
insta_password = '123123a$D'

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True,
                  multi_logs=True)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=77)

    # activity
    session.like_by_tags(["покупки", "product", "товар", "money", "almaty", "astana", "karaganda", "atyrau", "aktau"],
                         amount=3)

    session.set_do_follow(enabled=True, percentage=10, times=2)

session.follow_user_followers(['aliexpress.official', 'aliexpress', 'ebay', 'amazon'], amount=10, randomize=False,
                              sleep_delay=60)

session.follow_by_tags(['aliexpress', 'amazon', 'ebay'], amount=10)

session.unfollow_users(amount=126, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=655)
