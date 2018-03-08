merge-mp3.sh 依赖 ffmpeg 

text2speech.py 依赖 baidu-aip

安装baidu-aip:
 pip3 install baidu-aip
or:
 pip3 install -r requirements.txt


使用：
 1. __main__.py -d $mp3_dir filename.txt
 2. merge-mp3.sh $mp3_dir out_mp3_filename.mp3
