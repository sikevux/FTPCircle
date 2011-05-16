#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# vim:fileencoding=utf8

#Import all the moudles that should be in the README file.
import Main

#TODO: Write to file (only delete the last part of the file)
#TODO: Better markup
#TODO: Do not include modules/classes that is importet from standard library
for name in dir(Main):
	info = getattr(Main, name).__doc__
	if info != None:
		print name + ": \n" + info + "\n"
	