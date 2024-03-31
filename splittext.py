#!/usr/bin/env python3
#coding=utf-8
# date 2018-02-08 23:15:46
# author calllivecn <calllivecn@outlook.com>



import sys
import re

BAIDU_SPEECH_LIMIT=512

class SplitText:
    
    def __init__(self,filename):
        self.FILE = open(filename)
        self.BUF = 1024
        self.CUT_FLAG = '，。；,.;'
        self.S = []
        self.line = []
        self.re = re.compile(r'。+')

    def close(self):
        self.FILE.close()

    def _cut(self):
        """
        从txt文件里已self.CUT_FLAG组合整句
        """
        l = []
        data = self.FILE.read(self.BUF)

        data = "".join(data.replace('\n','。'))
        data = self.re.sub('。',data)

        data = self.line.copy() + data.split()
        self.line.clear()

        if not data:
            return []

        for ch_s in data:
            if ch_s == '':
                continue
            for ch in ch_s:
                if ch in self.CUT_FLAG:
                    self.line.append(ch)
                    l.append("".join(self.line))
                    self.line.clear()
                else:
                    self.line.append(ch)
        
        if not l:
            l.append("".join(self.line))
            self.line.clear()
                
        return l

    def _check(self,para):
        """
        check 一个单句有没有大于 BAIDU_SPEECH_LIMIT，大于就截断。
        """
        l = []
        for line in para:
            while True:
                line_len = len(line)
                if line_len > BAIDU_SPEECH_LIMIT:
                    l.append(line[0:BAIDU_SPEECH_LIMIT - 1])
                    line = line[BAIDU_SPEECH_LIMIT:]
                else:
                    if len(line) > 0:
                        l.append(line)
                    break
                    
        return l

    def getParagraph(self):
        """
        返回一个512字内的整句子，如果一个整句大于512字，截断返回512字。
        结束，返回空字符串。
        """
        string = ''
        str_len = 0
        while True:
            if len(self.S) > 0:

                if str_len <= BAIDU_SPEECH_LIMIT:
                    tmp = self.S.pop(0)
                    str_len += len(string)
                    string += tmp
                else:
                    break
                    
            elif self.S == []:
                self.S = self._check(self._cut())
                if self.S == []:
                    break

        return string


if __name__ == "__main__":
    st = SplitText(sys.argv[1])
    txt = True
    i=0
    while txt:
        txt = st.getParagraph()
        print((i,txt))
        i+=1
    st.close()

