#!/usr/bin/env python
# -*-coding: utf-8 -*-
# vim: sw=4 ts=4 expandtab ai
#ЗАДАЧА № 676 Игра со спичками

with open("INPUT.txt", "r") as files:
    n = int(files.read())

with open("OUTPUT.txt", "w") as files:
    if n % 3 == 0:
        files.write("2")
    else:
        files.write("1")
