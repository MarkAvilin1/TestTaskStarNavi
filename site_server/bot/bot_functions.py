from faker.providers import internet
from faker import Faker
import requests
import random
import json

fake = Faker()
fake.add_provider(internet)

# Class including function to calculate the number of posts and like status
class Bot(object):
    def __init__(self, number_of_users, max_user_posts, max_user_likes, url):
        self.number_of_users = number_of_users
        self.max_user_posts = max_user_posts
        self.max_user_likes = max_user_likes
        self.url = url

    # Make registration
    def register_user(self):
        data = {'username': fake.user_name(),
                'password': fake.password(length=16, special_chars=True, digits=True, upper_case=True, lower_case=True),
                'email': fake.email()}
        response = requests.post(url=self.url + 'api/v1/register/', data=data)
        if response.status_code == 201:
            login_response = requests.post(url=self.url + 'api/v1/login', data={'username': data.get('username'),
                                                                                'password': data.get('password')})
            auth_data = json.loads(login_response.content)
            return auth_data
        return None

    # Get the number of posts
    def get_posts(self, auth_data):
        post_counter = 0
        for _ in range(random.randint(1, int(self.max_user_posts))):
            post_data = {
                'post': fake.text(ext_word_list=None)
            }
            response = requests.get(url=self.url + 'api/v1/posts', data=post_data)
            if response.status_code >= 200:
                post_counter += 1
        return post_counter

    # Get the number os likes or dislikes
    def get_like_status(self, auth_data):
        actions = 0
        while actions < random.randint(1, int(self.max_user_likes)):
            response = requests.get(url=self.url + 'api/v1/likes/')
            if response.status_code >= 200:
                requests.get(url=self.url + 'api/v1/likes/')
            actions += 1
        return actions
