#!/usr/bin/python3
# script that distributes an archive to your web servers
from fabric.api import *
import os 

env.hosts = ['34.75.200.174', '34.229.85.234']


def do_deploy(archive_path):
    """ distributes an archive to web servers """
    status = True
    if os.path.exists(archive_path) is False:
        return False
    # Upload the file
    if put('{}'.format(archive_path), '/tmp/').failed is True:
        status = False
    file_local = archive_path.split('/')[-1]
    file_server = file_local.split('.')[0]
    # Create the folder
    if run("sudo mkdir -p /data/web_static/releases/{}/".
           format(file_server)).failed is True:
        status = False
    # Decompress the file into server
    if run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file_local, file_server)).failed is True:
        status = False
    # Delete the file from tmp
    if run("sudo rm -rf /tmp/{}".format(file_local)).failed is True:
        status = False
    # Move the file
    if run("sudo mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".
           format(file_server, file_server)).failed is True:
        status = False
    # Delete the archive from the web server
    if run("sudo rm -rf /data/web_static/releases/{}/".
           format(file_server)).failed is True:
        status = False
    # Delete the symbolic link
    if run("sudo rm -rf /data/web_static/current").failed is True:
        status = False
    # Delete the symbolic link
    if run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(file_server)).failed is True:
        status = False
    return status
