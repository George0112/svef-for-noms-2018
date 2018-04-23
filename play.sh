#!/bin/bash

python demo.py
./nalufilter originaltrace-rdo.txt receivedtrace.txt 5000 30 > filteredtrace.txt
./BitStreamExtractorStatic Soccer.264 Soccer-filtered.264 -et filteredtrace.txt
./H264AVCDecoderLibTestStatic Soccer-filtered.264 Soccer-filtered.yuv
rm -f Soccer-concealed.yuv
sudo ./framefiller filteredtrace.txt 608256 300 Soccer-filtered.yuv Soccer-concealed.yuv
./PSNRStatic 704 576 SOCCER52_origin.yuv Soccer-concealed.yuv > psnrtrace.txt	
python pltpsnr.py
mplayer -demuxer rawvideo -rawvideo w=704:h=576 Soccer-concealed.yuv
