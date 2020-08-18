#!/usr/bin/python3
""" Fabric script that generates a .tgz archive """
from datetime import datetime
from fabric.api import *
import os

env.hosts = ['34.75.200.174', '34.229.85.234']


def do_pack():
    """ function that packs archives """
    local('mkdir -p versions')
    date = datetime.now()
    tarfile = local('tar -cvzf versions/web_static_{}{}{}{}{}{}.tgz web_static'
                    .format(date.year, date.month, date.day,
                            date.hour, date.minute, date.second), capture=True)
    if tarfile.succeeded:
        return tarfile
    return None


def do_deploy(archive_path):
    """ distributes an archive to the
        web server """
    if os.path.exists(archive_path) is False:
        return False
    try:
        arc = archive_path.split('/')[-1]
        path = '/data/web_static/releases'
        directory = arc.split('.')
        put("{}".format(archive_path), "/tmp/{}".format(arc))
        run("sudo mkdir -p {}/{}/".format(path, directory[0]))
        run("sudo tar -xzf /tmp/{} -C {}/{}/".format(arc, path, directory[0]))
        run("sudo rm /tmp/{}".format(arc))
        run("sudo mv {}/{}/web_static/* {}/{}/\
            ".format(path, directory[0], path, directory[0]))
        run("sudo rm -rf {}/{}/web_static".format(path, directory[0]))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf {}/{}/ /data/web_static/current\
            ".format(path, directory[0]))
        print('New version deployed!')
        return True
    except Exception:
        return False


def deploy():
    """ deploy the functions """
    retpack = do_pack()
    if retpack is None:
        return False
    else:
        return do_deploy(retpack)
