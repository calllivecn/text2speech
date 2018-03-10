## 使用baidu-aip 把txt文本，转成mp3。

merge-mp3.sh 依赖 ffmpeg命令 

text2speech.py 依赖 baidu-aip

### 安装ffmpeg依赖

`apt install ffmpeg`

### 安装baidu-aip:

`pip3 install baidu-aip`

or:

`pip3 install -r requirements.txt`

### 使用：
1. \_\_main\_\_.py -d $mp3\_dir filename.txt
2. merge-mp3.sh $mp3\_dir out\_mp3\_filename.mp3

### 详细用法：

* \_\_main\_\_.py --help
