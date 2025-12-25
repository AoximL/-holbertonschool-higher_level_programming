#!/usr/bin/python3

"""  
this file is using with open so you can read files from python
"""
def read_file(filename=""):

   """  
   this file is using with open so you can read files from python
   """
   with open(filename, "r", encoding=utf8) as f:

     print(f.read())
