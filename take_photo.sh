#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

fswebcam -r 800x600 --no-banner /home/pi/data/$DATE.jpg
