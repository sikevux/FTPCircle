#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# vim:fileencoding=utf8

import sys
import getopt
from Main import FTPConnector, ConnectionInfo, ServerList


class BasicCLI():
	"""Class for creating and handling the very basic CLI"""
	def __init__(self):
		self._server_list = ServerList()
		self._server_list_matrix = self._server_list.make_matrix()
		self._ftp_connector = FTPConnector(self._server_list_matrix)
		print "Welcome to FTPCircle!\nArguments: list, download, help, exit"
		while True:
			luser_input = raw_input(">> ")
			if luser_input == "list":
				self._ftp_connector.list()
			elif luser_input == "exit":
				sys.exit()
			elif luser_input.startswith("download "):
				download_list = luser_input.split(" ")
				print download_list[1]
				#TODO: Download it
			elif luser_input in ("help", "h", "?"):
				self.usage()
			else:
				print "Your input was:", luser_input
	def usage(self):
		"""Handles the usage"""
		print "Arguments: list, download, help, exit\nlist: List folders on all servers\ndownload: Downloads file\nhelp: Prints this message\nexit: Exits this program"

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



