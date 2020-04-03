from django.shortcuts import render

# https://docs.djangoproject.com/en/3.0/ref/request-response/
# https://docs.djangoproject.com/en/3.0/intro/tutorial01/
# https://mkyong.com/python/python-how-to-list-all-files-in-a-directory/
# https://www.w3schools.com/python/python_try_except.asp
# https://stackoverflow.com/questions/4690600/python-exception-message-capturing

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse

# Import the libraries
import os
import glob
import json
import math
import numpy as np
import pandas as pd
import requests
from datetime import datetime

dirpath = os.path.dirname(os.path.realpath(__file__))
if not os.path.exists(dirpath + '/data'):
    os.makedirs(dirpath + '/data')

#def index(request):
    # return HttpResponse("Hello, world! You're at the polls index.")
    # response = HttpResponse()
    # response.write("<p>Here's the text of the Web page.</p>")
    # response.write("<p>Here's another paragraph.</p>")
    # return response
    # return  JsonResponse({'foo': 'bar'})

def index(request):
    try:
        with open(dirpath + '/data/' + request.GET["id"] + '.json') as json_file:
            dataread = json.load(json_file)
        status = 200
    except OSError as e:
        dataread = {'result': False, 'error': str(e), 'date': datetime.now()}
        status = 404
    except Exception as e:
        status = 500
        dataread = {'result': False, 'error': 'Enter valid ID', 'msg': str(e), 'date': datetime.now()}
    return JsonResponse(dataread, status=status)


URLArr = ['MPS', 'AP31', 'AB16', 'BAF', 'BF04', 'BA10', 'BA08', 'BI14', 'BI', 'BPC',
        'C', 'CI11', 'DRL', 'EM', 'GAI', 'GI01', 'HCL02', 'HDF', 'HDF01', 'HHM',
        'HI', 'HU', 'ICI02', 'IIB', 'IT', 'IOC', 'ITC', 'JSW01', 'KMB', 'LT',
        'MM', 'MS24', 'NI', 'NTP', 'ONG', 'PGC', 'RI', 'SBI', 'SC12', 'SPI',
        'TM03', 'TIS', 'TCS', 'TM4', 'TI01', 'UTC01', 'UP04', 'SG', 'W', 'ZEE']

def getdata(request):
    try:
        # Get the stock quote
        for i in URLArr:
            url = 'https://www.moneycontrol.com/mc/widget/basicchart/get_chart_value?dur=max&sc_did=' + i
            data = requests.get(url).json()
            data.update({'id': i})
            # Writing to json file
            with open(dirpath + '/data/'+i+'.json', 'w') as outfile:
                outfile.write(json.dumps(data))
            print(i)
        return JsonResponse({'result': True})
    except Exception as e:
        return JsonResponse({'result': False, 'msg': str(e), 'date': datetime.now()}, status = 500)


def listfiles(request):
    folders = [f for f in glob.glob(
        dirpath + "/data" + "**/*", recursive=True)]
    return JsonResponse({'size': len(folders), 'date': datetime.now(), 'result': folders})
