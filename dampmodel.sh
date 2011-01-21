#!/bin/sh
#django-admin.py dumpdata --database=/media/work/draft/club --natural
#django-admin.py dumpdata --locale=/media/work/draft/club --database=database.sqlite --natural
python manage.py dumpdata $1 --indent=1 --natural > $1.json