#!/bin/sh
lftp -e "mirror -R /home/pi/technaka/img /www/photos" -u $USER,$PASSWD ftp.cluster020.hosting.ovh.net


