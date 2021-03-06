#-*-coding:utf-8-*-

import config
import requests

TOKEN = ''

def test():
    url = config.URL + config.TEST
    r = requests.get(url)
    return r.content

def sendSound():
    TOKEN = ''
    url = config.URL + config.COUGH
    headers =\
            {
                'Cache-Control': 'no-cache',
                'Content-Type': 'multipart/form-data; boundary=<calculated when request is sent>',
                'Content-Length':'<calculated when request is sent>',
                'Host':'<calculated when request is sent>',
                'User-Agent':'PostmanRuntime/7.26.8',
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive'            
            }
    files =\
            {
                'cough':open('./output/sound.mp3', 'rb')        
            }
    r = requests.post(url, files=files)
    print("你获得新冠的概率是:")
    print(eval(r.content)['rate'])

def sendPic():
    url = config.URL + config.FIGURE
    headers =\
            {
                'coughtoken':'coughtoken From Coughchecker API',
                'Cache-Control':'no-cache',
                'Content-Type':'multipart/form-data; boundary=<calculated when request is sent>',
                'Content-Length':'<calculated when request is sent>',
                'Host':'<calculated when request is sent>',
                'User-Agent':'PostmanRuntime/7.26.8',
                'Accept':'*/*',
                'Accept-Encoding':'gzip, deflate, br',
                'Connection':'keep-alive'            
            }
    header = {'coughtoken': TOKEN}
    files = {"figure": open("./output/pic.jpg", "rb")}
    r = requests.post(url, files=files, headers=header)
    print(r.content)

