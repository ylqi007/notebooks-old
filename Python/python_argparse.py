#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/15/20 8:42 PM
# @Author  : Shark
# @Site    : 
# @File    : python_argparse.py
# @Software: PyCharm

import argparse

parser = argparse.ArgumentParser(description="A toy argument parser")
parser.add_argument('--param1', action='store_true')
parser.add_argument('--param2', action='store_true')

parser.add_argument('--foo', action='store_true')
parser.add_argument('--bar', action='store_true')
parser.add_argument('--baz', action='store_true')

args = parser.parse_args()
print(args)

# args1 = parser.parse_args(['--foo', '--bar'])
# print(args1)