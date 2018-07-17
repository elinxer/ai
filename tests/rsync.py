# linben build at 2018-03-12
# -*- coding: utf-8 -*-
# py2.x

from fabric.api import *

from fabric.contrib.files import exists
from fabric.colors import *
import os


env.user = 'deploy'
env.password = 'a5v!pDR#X^27'
# env.key_filename = "/home/deploy/id_rsa"
env.roledefs = {
    'app_s2': ['172.16.12.42'],
    'app_s1': ['10.132.8.12:512']
}


def runcmd(cmd):
    run('%s' % cmd)
    # print(green("This text is green!"))


@roles('app_s1')
def rsync_s1():
    run('rsync -avz --password-file=/tmp/rs_pw.txt --delete --exclude-from=/data/dmz/huazhen-20170921/.code huazhen@172.16.12.45::hz_app/flowertown/ /data/dmz/huazhen-20170921 |tee /tmp/rsync.log')
    print(green("============The rsync S1 had finished succeeful!!!=============="))


@roles('app_s2')
def rsync_s2():
    run('rsync -avz --password-file=/tmp/rs_pw.txt --delete --exclude-from=/data/sites/flowertown/.code huazhen@172.16.12.45::hz_app/flowertown /data/sites/ |tee /tmp/rsync.log')
    print(green("============The rsync S2 had finished succeeful!!!=============="))


def git_rsync():
    execute(rsync_s1)
    execute(rsync_s2)


def putfile():
    put('/data/sites/flowertown/.code', '/data/dmz/huazhen-20170921')


"""

fab -f /home/deploy/sh_dir/fab.py git_rsync

https://blog.csdn.net/wklken/article/details/8719541

"""
