#!/bin/bash

frames_folder=/tmp/frames
PYTHONPATH=.. python day10.py
mogrify -shave 40x40 $frames_folder/*.png
ffmpeg -framerate 10 -i $frames_folder/frame_%05d.png -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" /tmp/_day10.gif
gifsicle --optimize=3 --colors 256 --loopcount=0 -o /tmp/day10.gif /tmp/_day10.gif
