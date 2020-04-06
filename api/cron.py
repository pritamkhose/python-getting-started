from django.http import JsonResponse

# Import the libraries
import os
import glob
import json
from datetime import datetime

# https://gutsytechster.wordpress.com/2019/06/24/how-to-setup-a-cron-job-in-django/
# python3 manage.py crontab show
# python3 manage.py runserver
# python3 manage.py crontab add
# python3 manage.py crontab remove

dirpath = os.path.dirname(os.path.realpath(__file__))
if not os.path.exists(dirpath + '/data'):
    os.makedirs(dirpath + '/data')
# your functionality goes here
print(str(dirpath))
data = { 'date': str(datetime.now()), 'dirpath': str(dirpath), 'msg':'direct'} 
# Writing to json file
with open(dirpath + '/data/myfile.json', 'w') as outfile:
    outfile.write(json.dumps(data))     #  {"date": "2020-04-05 15:09:01.859980"}

def my_cron_job():
    dirpath = os.path.dirname(os.path.realpath(__file__))
    # your functionality goes here
    print('my_cron_job', dirpath)
    data = { 'date': str(datetime.now()), 'dirpath': str(dirpath), 'msg':'my_cron_job'} 
    # Writing to json file
    with open(dirpath + '/data/myfile.json', 'w') as outfile:
        outfile.write(json.dumps(data))     #   {"date": "2020-04-05 15:09:01.859980"}
