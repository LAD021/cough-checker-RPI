#!/usr/bin/python
#-*-coding:utf-8-*-

from cmd import Cmd
import os
import sys
import config
import sound
import pic
import request

class Client(Cmd):

    prompt = '''请按对应键：
    1)录入咳嗽
    2)录入照片
    3)上传数据
    4)退出
>'''
    intro = '''********************
    新冠咳嗽测试：
********************'''

    def __init__(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        Cmd.__init__(self)

    def do_exit(self, arg):
        print("再见！")
        return 0

    def do_1(self, arg):
        sound.getSound()

    def do_2(self, arg):
        pic.getPic()

    def do_3(self, arg):
        request.sendSound()
        request.sendPic()

    def do_4(self, arg):
        print("再见！")
        quit(0)

if __name__ == '__main__':
    os.system('clear')
    client = Client()
    client.cmdloop()

