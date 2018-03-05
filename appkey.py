#!/usr/bin/env python3
#coding=utf-8
# date 2018-03-03 23:49:33
# author calllivecn <c-all@qq.com>

import json


def appKey(APP_KEY='aip-key-id.json'):
    with open(APP_KEY) as f:
        conf = json.load(f)

    app_id = conf.get("APP_ID")
    api_key = conf.get("API_KEY")
    secret_key = conf.get("SECRET_KEY")
    if app_id and api_key and secret_key:
        return app_id ,api_key ,secret_key
    else:
        print(APP_KEY,'错误.')
        exit(2)

if __name__ == "__main__":
    print(appKey())
