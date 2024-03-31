#!/usr/bin/env python3
#coding=utf-8
# date 2018-02-08 23:08:18
# author calllivecn <calllivecn@outlook.com>


import time

from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '你的 App ID'
API_KEY = '你的 Api Key'
SECRET_KEY = '你的 Secret Key'

class Text2Speech:

    def __init__(self,APP_ID,API_KEY,SECRET_KEY,user_id='zhangxu'):
        self.aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
        self.user_id = user_id

    def t2s(self,text):

        while True:

            try:
                result = self.aipSpeech.synthesis(text[1],'zh',1,
                            {'cuid':self.user_id,'vol':7,'per':3}) 
            except Exception as e:
                print('\x1b[31m合成异常。重试ing\x1b[0m',text)
                time.sleep(1)
                continue

            if isinstance(result,dict):
                if result.get('error_code') in [500,501,502,503]:
                    print('\x1b[31m错误code:\x1b[0m',result)
                
                print('\x1b[31m出错重试ing\x1b[0m',text)
                time.sleep(1)
                continue
            else:
                return result

            break
