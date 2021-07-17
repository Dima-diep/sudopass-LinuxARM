#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
print("Old password:")
a = input()
print("New password:")
b = input()

with open("/home/rootpass/pass.py", "r") as f:
    raw = f.read().lower().replace(a, b)
    file = open("/home/rootpass/pass.py", "w")
    file.write(raw)
    file.close()
    f.close()
