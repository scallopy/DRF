# DRF

```
$ python --version
2.7.13
$ which python3.8
/usr/local/bin/python3.8
$ alias python="/usr/local/bin/python3.8"
$ python --version
Python 3.8.4
$ python3.8 -m django --version
3.1.1
$ nvirtualenv -p python3.8 env --no-site-packeges
$ source env/bin/activate
$ python3.8 -m pip install Django==3.1.1
$ django-admin --version
3.1.1
$ django-admin startproject drf
$ cd drf
$ python3.8 manage.py startapp fbvPassenger

```

## in drf/settings.py

```
...
INSTALLED_APPS = [
    ...
    'rest_framework',
    'fbvPassenger',
]
...

```
$ python3.8 manage.py makemigrations
$ python3.8 manage.py migrate

```


