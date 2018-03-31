#!/bin/bash

./nalufilter originaltrace-frameno.txt receivedtrace.txt 5000 30 > filteredtrace.txt
./BitStreamExtractorStatic BBB.264 BBB-filtered.264 -et filteredtrace.txt
./H264AVCDecoderLibTestStatic BBB-filtered.264 BBB-filtered.yuv
rm -f BBB-concealed.yuv
./framefiller originaltrace-frameno.txt 152064 240 BBB-filtered.yuv BBB-concealed.yuv
./PSNRStatic 352 288 BBB.yuv BBB-concealed.yuv
mplayer -demuxer rawvideo -rawvideo w=352:h=288 BBB-concealed.yuv
