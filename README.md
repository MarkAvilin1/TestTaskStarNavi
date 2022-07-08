# API created by Django REST_FRAMEWORK

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
/api/analytics/?date_from=2020-02-02&date_to=2020-02-15 . API should return analytics aggregated
by day.
● user activity an endpoint which will show when user was login last time and when he mades a last
request to the service.

Links:
1. Admin login 
>> http://127.0.0.1:8000/admin/
2. Register new user:
>> http://127.0.0.1:8000/api/v1/register/
3. User login
>> http://127.0.0.1:8000/api/v1/login/
4. User logout
>> http://127.0.0.1:8000/api/v1/logout/
5. All users logout
>> http://127.0.0.1:8000/api/v1/logoutall/
6. Get user last activity
>> http://127.0.0.1:8000/api/v1/activity/
7. Create new posts
>> http://127.0.0.1:8000/api/v1/create_post/
8. Show posts
>> http://127.0.0.1:8000/api/v1/posts/
9. Put new likes or dislikes
>> http://127.0.0.1:8000/api/v1/put_likes/
10. Show likes status
>> http://127.0.0.1:8000/api/v1/likes/
11. Get posts by date period 
>> http://127.0.0.1:8000/api/v1/post/analytics/date_from=<date_from>&date_to=<date_to>/
12. Get Token code
>> http://127.0.0.1:8000/api/v1/token/
13. Put refresh Token code to get new access Token code
>> http://127.0.0.1:8000/api/v1/token/refresh/'
14. Verify Token code 
>> http://127.0.0.1:8000/api/v1/token/verify/'
