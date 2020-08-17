#!/usr/bin/python3
""" Fabric script that generates a .tgz archive """
from fabric.api import local
from datetime import datetime


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
