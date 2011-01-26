#!/bin/sh
#django-admin.py dumpdata --database=/media/work/draft/club --natural
#django-admin.py dumpdata --locale=/media/work/draft/club --database=database.sqlite --natural
python manage.py dumpdata auth contenttypes accounts classifiers drugs services standards --indent=1 --natural > initial_data.json