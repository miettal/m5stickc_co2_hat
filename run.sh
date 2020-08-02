#!/bin/bash
ampy --port /dev/tty.usbserial-9952ED6393 put ntptime.py /flash/ntptime.py
ampy --port /dev/tty.usbserial-9952ED6393 put slack.py /flash/slack.py
ampy --port /dev/tty.usbserial-9952ED6393 put test_CO2_Ambient.py /flash/apps/test_CO2_Ambient.py 
