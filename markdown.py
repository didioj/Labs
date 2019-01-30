"""
 Markdown.py
 0. just print whatever is passed in to stdin
 0. if filename passed in as a command line parameter, 
    then print file instead of stdin
 1. wrap input in paragraph tags
 2. convert single asterisk or underscore pairs to em tags
 3. convert double asterisk or underscore pairs to strong tags

"""

import fileinput
import re

def convertStrong(line):
  line = str(re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line))
  line = str(re.sub(r'__(.*)__', r'<strong>\1</strong>', line))
  return line

def convertEm(line):
  line = str(re.sub(r'\*(.*)\*', r'<em>\1</em>', line))
  line = str(re.sub(r'_(.*)_', r'<em>\1</em>', line))
  return line

def convert3hash(line):
  line = str(re.sub(r'\#\#\#(.*)\#\#\#', r'<h3>\1</h3>', line))
  return line

def convert2hash(line):
  line = str(re.sub(r'\#\#(.*)\#\#', r'<h2>\1</h2>', line))
  return line

def converthash(line):
  line = str(re.sub(r'\#(.*)\#', r'<h1>\1</h1>', line))
  return line

foundblock = False
for line in fileinput.input():
  line = line.rstrip() 
  if ">" in line:
    if not foundblock:
      line = line.replace(">", "<blockquote>")
      foundblock = True
    elif foundblock:
      line = line.replace(">", "</blockquote>")
      foundblock = False  
  line = convertStrong(line)
  line = convertEm(line)
  line = convert3hash(line)
  line = convert2hash(line)
  line = converthash(line)
  
  print('<p>' + line + '</p>', end='')