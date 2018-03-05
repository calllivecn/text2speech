#!/bin/bash
# date 2018-02-27 16:14:50
# author calllivecn <c-all@qq.com>

lists='mp3.lists'

:> $lists

if [ -z "$1" ];then
	echo "指定一个输出文件."
	exit 1
fi


for mp3 in "tdir"/*;
do
	#echo "file ${mp3}"
	echo "file ${mp3}" >> $lists
done

ffmpeg -f concat -i $lists -acodec copy "$1"

if [ $? -ne 0 ];then
	echo "合成mp3出错.."
	exit 1
fi

rm $lists
rm -r tdir && mkdir tdir
