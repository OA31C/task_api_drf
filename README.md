API Posts and vote
=========

Api application, thanks to which you can create posts, comment on posts, and vote for posts you like.
It is also possible to create a user so log in.

Getting started
---------------

Download [Docker Desktop](https://www.docker.com/products/docker-desktop) for Mac or Windows. [Docker Compose](https://docs.docker.com/compose) will be automatically installed. On Linux, make sure you have the latest version of [Compose](https://docs.docker.com/compose/install/). 


## Start projects
Run in this directory
---------------------
{} ---> replace it with a value
*** ---> replace it with a value
---------------------

Create migration:
```
docker-compose run web python manage.py makemigrations
```

Use migration:
```
docker-compose run web python manage.py migrate
```

Create superuser:
```
docker-compose run web python manage.py createsuperuser
```

Run project:
```
docker-compose up
```

Get user token to authentication:
```
curl -d 'username=***&password=***'  http://0.0.0.0:5000/api/login/
```

Create user:
```
curl POST -d 'username=***&email=***&password=***'  http://0.0.0.0:5000/api/users/
```
#98f080e4d2ae1e9f5ef9333a8f1c70d0f3b12d4b
Get posts:
```
curl -H "Authorization: Token {this number token}" http://0.0.0.0:5000/api/posts/
```

Create post:
```
curl POST -d 'title=***&link=***&author=***' -H "Authorization: Token {this number token}" http://0.0.0.0:5000/api/posts/
```

Put post:
```
curl PUT -d 'title=***&link=***&author=***' -H "Authorization: Token {this number token}" http://0.0.0.0:5000/api/posts/{num_post_id}/
```

Get comments:
```
curl -H "Authorization: Token {this number token}" http://0.0.0.0:5000/api/comments/
```

Add comments:
```
curl POST -d 'post={post.id}&author={author.id}&content={Content}' -H "Authorization: Token 98f080e4d2ae1e9f5ef9333a8f1c70d0f3b12d4b" http://0.0.0.0:5000/api/comments/
```

Up vote post:
```
curl POST -d 'user=1&post=3&value=1' -H "Authorization: Token 98f080e4d2ae1e9f5ef9333a8f1c70d0f3b12d4b" http://0.0.0.0:5000/api/posts/{post.id}/upvote/
```

### Endpoints
* http://0.0.0.0:5000/api/users/  - api for users 
* http://0.0.0.0:5000/api/posts/  - api for posts
* http://0.0.0.0:5000/api/comments/ - api for comments
* http://0.0.0.0:5000/api/posts/id_post/upvote  - api for upvote post
