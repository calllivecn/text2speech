#!/usr/bin/env python3
#coding=utf-8
# date 2018-02-10 02:07:40
# author calllivecn <calllivecn@outlook.com>


import sys
from random import random
from time import sleep
from os.path import join,isfile,isdir
from queue import Queue
from threading import Thread
from argparse import ArgumentParser,ArgumentTypeError

import appkey
from text2speech import Text2Speech
from splittext import SplitText

APP_ID ,API_KEY ,SECRET_KEY = appkey.appKey()

def seq(num, max_num=10):
    """
    把一系列序号转换成一个等长字符串，用于一系列有序的文件名
    """
    num_str = str(num)

    if len(num_str) > max_num:
        raise ValueError('seq(num, max_num=10): argv num > max_num=10')

    while len(num_str) < max_num:
        num_str = '0' + num_str

    return num_str
        
def RandomSleep():
    sleep(random())

DONE = "is_done"
task_q = Queue(200)
result_q = Queue(200)

def worker_task(txtfile):
    """
    把任务加入任务队列
    """
    st = SplitText(txtfile)
    i = 0
    text = True
    while text:
        text = st.getParagraph()

        if text == '':
            print('任务布置结束。。。')
            task_q.put(DONE)
            break

        task_q.put((seq(i),text))
        i += 1



def worker_th_task(verbose=False):
    t2s = Text2Speech(APP_ID,API_KEY,SECRET_KEY)
    while True:

        task = task_q.get()

        if task == DONE:
            if task_q.empty():
                result_q.put(DONE)
                task_q.put(DONE)
                break
            else:
                task_q.put(DONE)
        else: 

            if verbose:
                print(task)
            speech = t2s.t2s(task)
            #RandomSleep();speech = b'a'
            result_q.put((task[0],speech))

def savespeech(filename,speech):
    with open(filename + '.mp3','w+b') as f:
        f.write(speech)

def worker_result(threads,output_dir='.'): # output_dir is cwd
    th_exit = 0
    while True:

        result = result_q.get()
        if result == DONE:
            th_exit += 1
            if th_exit >= threads:
                print('th_exit:',th_exit)
                break

        elif isinstance(result,tuple):
            path = join(output_dir,result[0])
            #print(path)
            savespeech(path,result[1])
        else:
            print('result_q.get() exception.')

## chech args
def _isdir(string):
    if isdir(string):
        return string
    else:
        raise ArgumentTypeError('{} is not directory'.format(string))

def _isfile(string):
    if isfile(string):
        return string
    else:
        raise ArgumentTypeError('{} is not txt file'.format(string))


def main():
    parse = ArgumentParser(usage='Using: %(prog)s [-tv] <txt> <mp3 '\
            'output directory>',
            description='把小说转换成mp3，使用baidu语音合成API.',
            epilog='NONE')
    parse.add_argument('-t','--threads',type=int,default=50,
            help='specify threads.')
    parse.add_argument('-v','--verbose',action='store_true',
            help='show verbose')
    parse.add_argument('-d','--dir',type=_isdir,required=True,
            help='specify directory.')
    parse.add_argument('txt',type=_isfile,
            help='txt text.')
    args = parse.parse_args()

    #print(args);exit(1)
    
    # start thread
    for _ in range(args.threads):
        th = Thread(target=worker_th_task,args=(args.verbose,),daemon=True)
        th.start()
        #print('th.start() -->',th.getName())

    th = Thread(target=worker_task,args=(args.txt,),daemon=True)
    th.start()

    worker_result(args.threads,args.dir)


main()
