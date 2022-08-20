# Raspberry Pi Bringup

## Setup
Currently trying to run `Raspbian Jessie with Pixel`

### Flash Micro SD on Mac
```
diskutil unmountDisk /dev/disk2
sudo dd if=~/Downloads/distro.img of=/dev/rdisk2
```

### OpenCV and bringup instructions
http://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/

### Screen
https://www.amazon.com/gp/product/B013JECYF2/ref=oh_aui_detailpage_o01_s00?ie=UTF8&psc=1
Prior to connecting the new display, do the following:

The only software you need is for the touchscreen. You can get this with `sudo apt-get install xinput-calibrator`

Then edit `/boot/config.txt` to add the following lines:
```
hdmi_group=2
hdmi_mode=1
hdmi_mode=87
hdmi_cvt 800 400 60 6 0 0 0
dtparam=spi=on
dtparam=i2c_arm=on

display_rotate=1 #if you want to rotate the screen 90 deg

dtoverlay=ads7846,cs=1,penirq=25,penirq_pull=2,speed=50000,keep_vref_on=0,swapxy=0,pmax=255,xohms=150,xmin=200,xmax=3900,ymin=200,ymax=3900 <======Note this is all on 1 line!

dtoverlay=w1-gpio-pullup,gpiopin=4,extpullup=1
```
Shutdown the pi, and connect the display. When you power it back up, you should have a perfect display. You can now calibrate the touchscreen by running `Menu-->Preferences-->Calibrate Touchscreen`.

## Cameras
https://www.amazon.com/gp/product/B01CVGBVM6/ref=oh_aui_detailpage_o01_s00?ie=UTF8&psc=1

`sudo apt-get install fswebcam`

### Resources

http://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/
http://www.pyimagesearch.com/2016/01/18/multiple-cameras-with-the-raspberry-pi-and-opencv/
http://www.pyimagesearch.com/2015/12/21/increasing-webcam-fps-with-python-and-opencv/

## updating apt-get for sources
```
sudo vim /etc/apt/sources.list (uncomment line)
sudo apt-get update
sudo apt-get build-dep python-matplotlib
```

--------------------
## Get it started
```
$ workon cv
$ cd code/
$ python run.py
```

## matplotlib
```
pip --no-cache-dir -U install matplotlib
```