#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# vim:fileencoding=utf8

import sys
import getopt
from Main import FTPConnector, ConnectionInfo, ServerList


class BasicCLI():
	u"""Class for creating and handling the very basic CLI"""
	def __init__(self, server_list_name):
		self._server_list = ServerList(server_list_name)
		self._server_list_matrix = self._server_list.make_matrix()
		self._ftp_connector = FTPConnector(self._server_list_matrix)
		print u"Welcome to FTPCircle!\nArguments: list, download, help, exit, serverlist"
		self.interface()

	def interface(self):
		self.luser_input = raw_input(u"-> ")
		if self.luser_input == u"list":
			self.interface_list()
		elif self.luser_input == u"exit":
			sys.exit()
		elif self.luser_input.startswith(u"download "):
			self.interface_download()
		elif self.luser_input in (u"help", u"h", u"?"):
			self.usage()
		elif self.luser_input.startswith(u"serverlist "):
			self.interface_serverlist()
		else:
			print (u"Your input was:", self.luser_input)

	def interface_download(self):
		#TODO: Download interface to download
		download_list = self.luser_input.split(u" ")
		print (download_list[1])
		#TODO: Download it
		self.interface()

	def interface_serverlist(self):
		#TODO: Serverlist interface to pipe to download interface and list interface
		server_list_name = self.luser_input.split(u" ")
		print (server_list_name[1])
		self.interface()

	def interface_list(self):
		#TODO: List interface to list
		self._ftp_connector.list()
		self.interface()

	def usage(self):
		u"""Handler for CLI usage"""
		print u"Arguments: list, download, help, exit\nlist: List folders on all servers\ndownload: Downloads file\nserverlist: Changes the list of servers to use\nhelp: Prints this message\nexit: Exits this program"
		self.interface()

class ArgumentHandler():
	u"""Usage: sumfile [-h help] [-d debug] [-s serverlist]"""
	def usage(self):
		u"""Handler for argument usage"""
		#TODO: Fix better usage
		print (self.__doc__)

	def help_arg(self):
		u"""Handler for help flag"""
		self.usage()
		sys.exit()

	def debug_arg(self):
		u"""Handler for debug flag"""
		global _debug
		_debug = 1

	def __init__(self, argv):
		try:
			opts, args = getopt.getopt(argv, u":hsd")
		except getopt.GetoptError:
			self.usage()
			sys.exit(2)
		#FULHACK!
		i=0
		for opt, arg in opts:
			i += 2
			if opt == u"-h":
				self.help_arg()
			elif opt == u"-d":
				self.debug_arg()
			elif opt == u"-s":
				try:
					server_list_name = sys.argv[i]
					BasicCLI(server_list_name)
				except IndexError:
					print u"No server list specified"
					sys.exit()

def main(argv):
	u"""Main function that passes the arguments that the user supplied to the argument handler"""
	ArgumentHandler(argv)
if __name__ == u"__main__":
	main(sys.argv[1:])
