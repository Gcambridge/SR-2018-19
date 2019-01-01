## networktest.py
+ ### 12.30.18:
  * 1 Hour on executing shell commands from python script and piping results to output file using `os` package
+ ### 1.1.19:
  * 2 Hours on writing results from multiple trials to same file and reading shell arguments.
 
## video_and_GPS.py
+ ###  12.26 - 12.27.18:
  * 3 Hours on multiprocessing, executing shell commands from python script, and outputing recorded video from both cameras, using RSYNC
  to transfer the video output from Raspberry Pi to PC.
+ ### 12.28 - 12.30.18:
  * 11 Hours on getting raw GPS data from serial device, installing and configuring GPSD and testing formated GPSD output.
Configuring GPSD to run as a Daemon and removing hardware conflict between shared use of embedded serial port on Raspberry Pi
took a long time due to lack of documentation by Adafruit. This was resolved by disabling bluetooth's use of the Pi's UART port
through the use of `pi3-disable-bt` overlay, added to `config.txt`.
+ ### 12.31.18:
  * 1 Hour spent experimenting with sending gps data to a node.js server. Exporting of raw data to web server and the export from 
  web server to converter and then to Google Maps was a long and complicated workflow that was rather slow. 
  * 2 Hours spent researching and testing mapping applications for use on the raspberry pi. Comparing foxtrotGPS and arcGIS, foxtrotGPS
    was less resource intensive and had better support for exporting GPSD data.


