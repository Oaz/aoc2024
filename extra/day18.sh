#!/bin/bash

frames_folder=/tmp/frames
PYTHONPATH=.. python day18.py
mogrify -shave 45x45 $frames_folder/*.png
ffmpeg -framerate 50 -i $frames_folder/frame_%05d.png -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" /tmp/_day18.gif
gifsicle --optimize=3 --colors 256 --loopcount=1 -o /tmp/day18.gif /tmp/_day18.gif
