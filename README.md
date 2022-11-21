## Welcome
# OCEAN BOOKS

## Tech

* [Django](https://www.djangoproject.com/) - is a high-level Python Web framework
* [Django REST framework](https://www.django-rest-framework.org/) - Django REST framework is a powerful and flexible toolkit for building Web APIs
* [Postgresql](https://www.postgresql.org/) - open source object-relational database system

And many other libraries.

Dillinger requires [Python](https://www.python.org) v3.4+.

```shell
$ git clone https://gitlab.com/Abduraxmonnn/chehol_api.git
$ cd chat_api
```

### Setting project

* Linux
```shell
$ virtualenv -p /usr/bin/python3 .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
```

* Windows
```shell
$ python -m venv ./venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
$ python manage.py migrate
```

* MacBook
```shell
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
```

### Development
```shell
$ python manage.py runserver