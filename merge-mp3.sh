#!/bin/bash
# date 2018-02-27 16:14:50
# author calllivecn <calllivecn@outlook.com>

lists='mp3.lists'


usage(){
	echo "Using: ${##/0} <mp3_dir> <outfilename>"
}

if [ ! -d "$1" ];then
	usage
	exit 1
else
	mp3_dir="${1%/}"
fi


if [ -z "$2" ];then
	usage
	exit 1
fi

:> $lists

for mp3 in "$mp3_dir"/*;
do
	#echo "file ${mp3}"
	echo "file ${mp3}" >> $lists
done

ffmpeg -f concat -i $lists -acodec copy "$2"

if [ $? -ne 0 ];then
	echo "ffmpeg 合成mp3出错.."
	exit 1
fi

rm $lists
rm -r tdir && mkdir tdir
