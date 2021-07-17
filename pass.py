#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import getpass
import os

passwd = getpass.getpass('root password: ')
if passwd == oldpass:
    break
elif passwd != oldpass:
    os.system("python3 ~/sudopass/pass.py")
