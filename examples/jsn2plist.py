#!/usr/bin/env python
#-*- coding: utf-8 -*-


import plistlib
import json


def plist2json(plist_file, output_file):
    plist = plistlib.readPlist(plist_file)
    json.dump(plist, open(output_file, "w"), indent=4, sort_keys=True)


def json2plist(json_file, output_file):
    converted_dict = json.load(open(json_file, "r"))
    plistlib.writePlist(converted_dict, output_file)