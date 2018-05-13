# -*- coding: utf-8 -*-
"""
Created on Fri May 11 17:28:13 2018

@author: Robert
"""

# Data Tools

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("echo")

args = parser.args()

print (args.echo)