! Project purpose

!Overview design
 
!!Installation

!!!Setup the environment

!!!Get the code

!!!Run it


!! Deployment

Ref:
The structure/formatting of this doc: django weekly http://djangoweekly.com/newsletter/ -> Projects -> https://github.com/bitpixdigital/django-next-train
----
!!Docker

--
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