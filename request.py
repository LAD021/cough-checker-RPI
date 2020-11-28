#-*-coding:utf-8-*-

import config
import requests

def test():
    url = config.URL + config.TEST
    r = requests.get(url)
    return r.content

def sendSound(data):
    url = config.URL + config.COUGH
    r = requests.post(url, data)
    print(r.content)

def sendPic(data):
    url = config.URL + config.FIGURE
    r = requests.post(url, data)
    print(r.content)

