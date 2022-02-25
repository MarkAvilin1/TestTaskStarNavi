from bot.bot_functions import Bot
import configparser

config = configparser.ConfigParser()
config.read('botconfig.ini')

if __name__ == "__main__":
    number_of_users = config['MAIN']['NUMBER_OF_USERS']
    max_user_posts = config['MAIN']['MAX_USER_POSTS']
    max_user_likes = config['MAIN']['MAX_USER_LIKES']
    url = config['MAIN']['URL']
    bot = Bot(number_of_users=number_of_users,
              max_user_posts=max_user_posts,
              max_user_likes=max_user_likes,
              url=url)
    posts_counter = 0
    like_dislike_counter = 0
    for _ in range(int(number_of_users)):
        auth_data = bot.register_user()
        posts_counter += bot.get_posts(auth_data=auth_data)
        like_dislike_counter += bot.get_like_status(auth_data=auth_data)
    print(
        f"@===> {number_of_users} users have created\n"
        f"@===> {posts_counter} posts have created\n"
        f"@===> {like_dislike_counter} likes or dislike have put")
