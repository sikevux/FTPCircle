#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# vim:fileencoding=utf8

import sys
import getopt
from Main import FTPConnector, ConnectionInfo, ServerList


class BasicCLI():
	"""Basic CLI"""
	def __init__(self):
		self._server_list = ServerList()
		self._server_list_matrix = self._server_list.make_matrix()
		self._ftp_connector = FTPConnector(self._server_list_matrix)
		while True:
			moo = raw_input(">> ")
			if moo == "list":
				self._ftp_connector.list()
			elif moo in ("exit", "quit"):
				sys.exit()
			print moo

class ArgumentHandler():
	"""Usage: sumfile [-h help] [-d debug] [-s serverlist]"""
	def usage(self):
		""" Handles the usage"""
		#TODO Fix better usage
		print self.__doc__

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
				print "m00"

def main(argv):
	""" Tralalalal """
	ArgumentHandler(argv)
if __name__ == "__main__":
	main(sys.argv[1:])



