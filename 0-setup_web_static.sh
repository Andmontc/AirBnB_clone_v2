#!/usr/bin/env bash
#script that sets up your web servers for the deployment
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i '/listen 80 default_server/a \\tlocation /hbnb_static/ {\n\t alias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
sudo /etc/init.d/nginx restart
exit 0
