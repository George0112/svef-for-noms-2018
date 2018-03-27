#!/bin/bash

./nalufilter originaltrace-frameno.txt receivedtrace.txt 5000 30 > filteredtrace.txt
./BitStreamExtractorStatic Soccer_SVC_growing_2860.264 Soccer_SVC_growing-filtered.264 -et filteredtrace.txt
./H264AVCDecoderLibTestStatic Soccer_SVC_growing-filtered.264 Soccer_SVC_growing-filtered.yuv
rm -f Soccer_SVC_growing-concealed.yuv
./framefiller originaltrace-frameno.txt 608256 1489 Soccer_SVC_growing-filtered.yuv Soccer_SVC_growing-concealed.yuv
./PSNRStatic 704 576 Soccer_SVC_growing_2860.264 Soccer_SVC_growing-concealed.yuv
mplayer -demuxer rawvideo -rawvideo w=704:h=576 Soccer_SVC_growing-concealed.yuv
