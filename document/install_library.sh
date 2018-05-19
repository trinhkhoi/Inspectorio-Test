#!/bin/bash
# install postgresql database relational
sudo apt-get install postgresql postgresql-contrib

# install pip
export LC_ALL=C
sudo apt-get install python3-setuptools
sudo apt-get install python3-pip

# install django framework
sudo pip3 install django
sudo pip3 install djangorestframework
sudo pip3 install django-filter
sudo pip3 install xlrd
sudo pip3 install psycopg2
sudo pip3 install psycopg2-binary