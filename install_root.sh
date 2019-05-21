#!/bin/bash
#Ment to be run as root after buildout is done. Will obtain cert and install on nginx debian

cd /etc/nginx
ln -s /home/voteit/srv/vision_buildout/etc/nginx.conf ./sites-available/vision.conf
cd sites-enabled
ln -s ../sites-available/vision.conf

service nginx stop
certbot certonly --standalone -d vision.voteit.se
service nginx start
