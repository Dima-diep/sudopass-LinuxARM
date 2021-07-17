#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os

with open("/root/.bashrc", "r") as f:
    raw = f.read().lower().replace("alias sudo='python3 /home/rootpass/pass.py && sudo'", " ")
    file = open("/root/.bashrc", "w")
    file.write(raw)
    file.close()
    f.close()

with open("/root/.zshrc", "r") as f:
    raw = f.read().lower().replace("alias sudo='python3 /home/rootpass/pass.py && sudo'", " ")
    file = open("/root/.zshrc", "w")
    file.write(raw)
    file.close()
    f.close()
os.system("cd ~ && sudo rm -rf /home/rootpass")
