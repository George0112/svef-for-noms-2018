#!/bin/bash

./nalufilter $1trace-rdo.txt receivedtrace.txt 1000 30 > filteredtrace.txt
./BitStreamExtractorStatic $1.264 out-filtered.264 -et filteredtrace.txt
./H264AVCDecoderLibTestStatic out-filtered.264 out-filtered.yuv
rm -f out-concealed.yuv
sudo ./framefiller filteredtrace.txt 608256 240 out-filtered.yuv out-concealed.yuv
echo $1_origin.yuv out-concealed.yuv
./PSNRStatic 704 576 $1_origin.yuv out-concealed.yuv > psnrtrace.txt	
python demo.py $1
python pltpsnr.py $1
mplayer -loop 0 -demuxer rawvideo -rawvideo w=704:h=576 out-concealed.yuv
