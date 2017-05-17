Tango with Django
=================
**Work quickly, safely, and without headaches. So I joined to use Django for web development.**

This is a little project that I keep as a record how I learn to use Django for web development. I mainly follow the tutorial of Tango with Django, however, it is not limited to the tutorial and should be more that it.

As I need a good record as a reference on how to develop with Django in the future, I plan each commit carefully.

## Purpose
<p align="center">
<img src="http://i.imgur.com/t6iC9TC.png">
<img src="https://www.spaghetti-western.net/images/thumb/7/73/DjangoSpecial_Banner.png/400px-DjangoSpecial_Banner.png">
</p>

## Design overview


Getting Started
===============

## Setup

To prevent breaking our system and prevent dependency hell, we are going to setup a development environment in virtual environment.

### The Setup process 1:
Setup a [virtual environment] (http://docs.python-guide.org/en/latest/dev/virtualenvs/) with [virtualenv] (https://pypi.python.org/pypi/virtualenv) and [virtualenvwrapper] (https://virtualenvwrapper.readthedocs.io/en/latest/index.html).

Firstly, install virtualenv and virtualenvwrapper.

    pip install virtualenv
    pip install virtualenvwrapper

And then execute a shell script to activate a virtual environment.

	source virtualenvwrapper.sh 

(Try `source /usr/local/bin/virtualenvwrapper.sh` instead if you cannot not activate a virtual environment succussfully. And please refer to the doc of virtualenvwrapper.)

Then create a virtual environment for the project, and then activate it.

	mkvirtualenv rango
	workon rango

(As we are going to execute Django on python 3, we should tell virtualenv where the python3 located by issuing `mkvirtualenv -p /usr/bin/python3.5 rango`, which the location of python3 could be found by issuing `whereis python3`)

When a `(rango)$` is shown on prompt, you are successfully in a virtual environment `rango`.

Once a virtual environment is setup, we are focus on Python stuffs now:

Check if you have Django installed with `pip list`:

	pip list

Install Django with `pip`:

	pip install django

This will install the latest stable Django. However, we should install all the required package with `requiruments.txt`.

	pip install -r requirements.txt

It will install the packages automatically with matching version.

### The Setup process 2:
Setup the environment with docker.

Refer to the official doc of docker on Django, we should prepare a `Dockerfile`, `requirements.txt` and `docker-compose.yml`:

	workon rango
	pip freeze > requirements.txt

And then create a project and execute the docker environment

	docker-compose run web django-admin.py startproject tango_with_django_project
	docker-compose up

(ref: https://docs.docker.com/compose/django/)

## Run it!

Edit `ALLOWED_HOSTS = []` in setting.py. Activate the virtual environment and then run the test server

	source virtualenvwrapper.sh # if the workon command does not recognized
	workon rango
	python manage.py runserver

## Deployment

Update the requirements.txt with the current packages by

	pip freeze > requirements.txt


Reference
=========

## General Ref:
* The structure/formatting of this doc: [README.md](https://github.com/git-up/GitUp/blob/master/README.md) of [GitUp](https://github.com/git-up/GitUp)
* The tutorial to build this project: [How to Tango with Django](http://www.tangowithdjango.com/)
* The design/style of the webpage: [django weekly](http://djangoweekly.com/newsletter/) -> Projects -> https://github.com/bitpixdigital/django-next-train
* Better understanding Python and what a web framework is: [Full Stack Python: Web frameworks](http://www.fullstackpython.com/web-frameworks.html)
* Semantic Version: https://forum.syncthing.net/t/best-cheap-arm-board-for-syncthing/9103 -> [restic] (https://restic.github.io) -> [Semantic Version](http://semver.org)
* Formatting of Python: https://pyformat.info

## Object oriented in Python
* [Everything I know About Python...: Improve Your Python: Python Classes and Object Oriented Programming](https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/)
* [doc.python.org: abc — Abstract Base Classes](https://docs.python.org/3/library/abc.html)

## Testing
* Google:Nose vs Pytest -> https://agopian.info/presentations/2015_06_djangocon_europe/ , [Comparison of py.test and nose for Python testing | Koodaamo](https://koodaamo.wordpress.com/2013/11/29/comparison-of-py-test-and-nose-for-python-testing/)
* [Python Testing](http://pythontesting.net) with markdown.py as an example

## API
* [“Create a Django API in Under 20 Minutes”] (https://medium.com/@scottdomes/create-a-django-api-in-under-20-minutes-2a082a60f6f3)
* Google: Django and Angular 2 -> [Reddit: Django with Angular 2/] (https://www.reddit.com/r/django/comments/51k896/django_with_angular_2/) -> [Slides.com: 5 quick tips django docker] (http://slides.com/jamespacileo/5-quick-tips-django-docker-4#/)

## Docker
* [Django by Docker Official Image] (https://store.docker.com/images/65765d71-d893-407d-a707-486c7381dfbf?tab=description)
* [Quickstrt: Compose and Django] (https://docs.docker.com/compose/django/)

## Git 
* [A successful Git branching model] (http://nvie.com/posts/a-successful-git-branching-model/) from [Git flow 開發流程] (https://ihower.tw/blog/archives/5140)

Docker Example:

ref: jun.oct-13.us/cn/node/60 -> jun.oct-13.us/cn/article/how-to-use-docker-drupal-create-webform

    # docker run --name drupaldb -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=drupal -d mariadb
    # docker run --name d8docker --link drupaldb:mysql -p 80:80 -d drupal:741

For using wordpress:
Google: wordpress docker -> https://hub.docker.com/_/wordpress/
Docker.com: mariadb -> 

For using wordpres with docker compose:
Google: wordpress docker -> https://docs.docker.com/compose/wordpress
Google: wordpress docker -> http://www.sitepoint.com/how-to-use-the-official-docker-wordpress-image/

Contributing
============

See [CONTRIBUTING.md](CONTRIBUTING.md).

Credits
=======

- [@swisspol](https://github.com/swisspol): concept and code
- [@wwayneee](https://github.com/wwayneee): UI design
- [@jayeb](https://github.com/jayeb): website

*Also a big thanks to the fine [libgit2](https://libgit2.github.com/) contributors without whom GitUp would have never existed!*

License
=======

GitUp is copyright 2015-2016 Aaron Law and available under [GPL v3 license](http://www.gnu.org/licenses/gpl-3.0.txt). See the [LICENSE](LICENSE) file in the project for more information.


Last update: 2017-03-23 01:27, Hong Kong
