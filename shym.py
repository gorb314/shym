#!/usr/bin/python

import sys
import re

PREFIX = sys.argv[1]

POINTERS = []
line = sys.stdin.readline()
while line:
	line = line.rstrip()
	if line == "from ctypes import *":
		break
	line = sys.stdin.readline()

while line:
	line = line.rstrip()
	m = re.search(r"restype = POINTER\((%s\w+)\)" % PREFIX, line)
	if m:
		POINTERS.append(m.group(1))
	print line
	line = sys.stdin.readline()

print POINTERS
print """
for name in dir():
	myvalue = eval(name)
	pointers = [POINTER(x) for x in [
# list of POINTER(x) structures that will be stripped
%s
	]]
	def stripPOINTER(func):
		def _newfunc(*args, **kwargs):
			obj = func(*args, **kwargs)
			try:
				return obj.contents
			except ValueError, e:
				return None
		return _newfunc
	try:
		if getattr(myvalue, 'restype'):
			if myvalue.restype in pointers:
				try:
					cmd = "%%s = stripPOINTER(%%s)" %% (name, name)
					#print cmd
					exec(cmd)
				except Exception, e:
					print e
	except:
		pass
""" % (",\n".join(POINTERS))

