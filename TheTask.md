# TestTaskStarNavi

Test task: python developer
Object of this task is to create a simple REST API. You can use one framework from this list (Django
Rest Framework, Flask or FastAPI) and all libraries which you are prefer to use with this frameworks.
1. Social Network
Basic models:
● User

● Post (always made by a user)
Basic Features:
● user signup

● user login

● post creation

● post like

● post unlike

● analytics about how many likes was made. Example url
/api/analitics/?date_from=2020-02-02&date_to=2020-02-15 . API should return analytics aggregated
by day.

● user activity an endpoint which will show when user was login last time and when he mades a last
request to the service.
Requirements:
● Implement token authentication (JWT is prefered)
Object of this bot demonstrate functionalities of the system according to defined rules. This bot
should read rules from a config file (in any format chosen by the candidate), but should have
following fields (all integers, candidate can rename as they see fit).
2. Automated bot
● number_of_users

● max_posts_per_user
STARNAVI
● number_of_users

● max_posts_per_user 

● max_likes_per_user

Bot should read the configuration and create this activity:

● signup users (number provided in config)

● each user creates random number of posts with any content (up to

max_posts_per_user)

● After creating the signup and posting activity, posts should be liked randomly, posts

can be liked multiple times
Notes:
● Clean and usable REST API is important

● Bot this is just separate python script, not a django management command or etc.

● the project is not defined in detail, the candidate should use their best judgment for every
non-specified requirements (including chosen tech, third party apps, etc), however

● every decision must be explained and backed by arguments in the interview

● Result should be sent by providing a Git url. This is a mandatory requirement.
