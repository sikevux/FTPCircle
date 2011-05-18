#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# vim:fileencoding=utf8

import sys
import getopt


class ArgumentHandler():
	"""Usage: sumfile [-h help] [-d debug] [-s serverlist]"""
	def usage(self):
		""" Handles the usage"""
		#TODO Fix better usage
y		print self.__doc__

	def help_arg(self):
		"""Handles the help flag"""
		self.usage()
		sys.exit()

	def debug_arg(self):
		"""Handles the debug flag"""
		global _debug
		_debug = 1

	def __init__(self, argv):
		try:
			opts, args = getopt.getopt(argv, ":hsd")
		except getopt.GetoptError:
			self.usage()
			sys.exit(2)

		for opt, arg in opts:
			if opt == "-h":
				self.help_arg()
			elif opt == "-d":
				self.debug_arg()
			elif opt == "-s":
				#TODO Handle serverlist
				
def main(argv):
	""" Tralalalal """
	ArgumentHandler(argv)
if __name__ == "__main__":
	main(sys.argv[1:])
