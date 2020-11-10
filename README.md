Task api django rest framework
=========

A simple api application 

Getting started
---------------

Download [Docker Desktop](https://www.docker.com/products/docker-desktop) for Mac or Windows. [Docker Compose](https://docs.docker.com/compose) will be automatically installed. On Linux, make sure you have the latest version of [Compose](https://docs.docker.com/compose/install/). 


## Start projects
Run in this directory:
```
docker-compose run web python manage.py makemigrations
```

```
docker-compose run web python manage.py migrate
```

```
docker-compose run web python manage.py createsuperuser
```

Run project:
```
docker-compose up
```


### Recomendations
* http://0.0.0.0:5000/api/users/  - api for users 
* http://0.0.0.0:5000/api/posts/  - api for posts
* http://0.0.0.0:5000/api/comments/ - api for comments
* http://0.0.0.0:5000/api/posts/id_post/upvote  - api for upvote post

