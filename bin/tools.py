#!/bin/python3
import configparser
import os.path
import sys
def root_path():
    config=configparser.ConfigParser()
    config.read(os.path.join(sys.path[0], "config.ini"))
    return config["id1fs"]["path"]



def status_path():
    return os.path.join(root_path(),"managers","status.json")


if __name__=="__main__":
    print(status_path())

