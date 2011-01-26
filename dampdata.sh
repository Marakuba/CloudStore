#!/bin/sh
python manage.py dumpdata auth contenttypes accounts classifiers drugs services standards --indent=1 --natural > initial_data.json