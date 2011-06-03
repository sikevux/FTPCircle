#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-
# vim:fileencoding=utf8

import sys
import getopt
from Main import FTPConnector, ConnectionInfo, ServerList

class BasicCLI():
	"""Class for creating and handling the very basic CLI"""
	def __init__(self, server_list_name):
		self._server_list = ServerList(server_list_name)
		self._server_list_matrix = self._server_list.make_matrix()
		self._ftp_connector = FTPConnector(self._server_list_matrix)
		print("Welcome to FTPCircle!\nArguments: list, download, help, exit, serverlist")
		self.interface()

	def interface(self):
		self.luser_input = input("-> ")
		if self.luser_input == "list":
			self.interface_list()
		elif self.luser_input == "exit":
			sys.exit()
		elif self.luser_input.startswith("download "):
			self.interface_download()
		elif self.luser_input in ("help", "h", "?"):
			self.usage()
		elif self.luser_input.startswith("serverlist "):
			self.interface_serverlist()
		else:
			print("Your input was:", self.luser_input)
		self.interface()

	def interface_download(self):
		#TODO: Download interface to download
		download_list = self.luser_input.split(" ")
		print (download_list[1])
		#TODO: Download it

	def interface_serverlist(self):
		#TODO: Serverlist interface to pipe to download interface and list interface
		server_list_name = self.luser_input.split(" ")
		print(server_list_name[1])

	def interface_list(self):
		#TODO: List interface to list
		self._ftp_connector.list()

	def usage(self):
		"""Handler for CLI usage"""
		print("Arguments: list, download, help, exit\nlist: List folders on all servers\ndownload: Downloads file\nserverlist: Changes the list of servers to use\nhelp: Prints this message\nexit: Exits this program")

class ArgumentHandler():
	"""Usage: sumfile [-h help] [-d debug] [-s serverlist]"""
	def usage(self):
		"""Handler for argument usage"""
		#TODO: Fix better usage
		print(self.__doc__)

	def help_arg(self):
		"""Handler for help flag"""
		self.usage()
		sys.exit()

	def debug_arg(self):
		"""Handler for debug flag"""
		global _debug
		_debug = 1

	def __init__(self, argv):
		try:
			opts, args = getopt.getopt(argv, ":hsd")
		except getopt.GetoptError:
			self.usage()
			sys.exit(2)
		#FULHACK!
		i=0
		for opt, arg in opts:
			i += 2
			if opt == "-h":
				self.help_arg()
			elif opt == "-d":
				self.debug_arg()
			elif opt == "-s":
				try:
					server_list_name = sys.argv[i]
					BasicCLI(server_list_name)
				except IndexError:
					print("No server list specified")
					sys.exit()

def main(argv):
	"""Main function that passes the arguments that the user supplied to the argument handler"""
	ArgumentHandler(argv)
if __name__ == "__main__":
	main(sys.argv[1:])
