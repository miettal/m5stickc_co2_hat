#!/bin/bash
echo ntptime.py
ampy --port /dev/tty.usbserial-9952ED6393 put ntptime.py /flash/ntptime.py
echo slack.py
ampy --port /dev/tty.usbserial-9952ED6393 put slack.py /flash/slack.py
echo main.py
ampy --port /dev/tty.usbserial-9952ED6393 put main.py /flash/apps/main.py 
