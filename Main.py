#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from ftplib import FTP
from ftplib import FTP_TLS
import socket

class FTPConnector():
	""" Class that connects to the FTP servers and takes care of interfaceing with the FTP"""
	_connected = False
	_server_list = []

	def __init__(self, server_list):
		self._server_list = server_list

	def connect(self):
		"""Connects to all of the servers listed in _server_lsit"""
		if self._connected:
			print "Already connected"
			return None 
			#TODO: Save connection instances. 
		else:
			print "Not connected.\n"
			print "Connnecting... \n"
			connections = []
			if len(self._server_list) == 0 :
				print "No servers where specified. \n"
			else:
				i=0
				for line in self._server_list:
					try:
						if self._server_list[i][3] == 1:
							ftp = FTP_TLS(self._server_list[i][0], self._server_list[i][1], self._server_list[i][2])
						else:
							ftp = FTP(self._server_list[i][0], self._server_list[i][1], self._server_list[i][2])
					except socket.error, msg:
						print "SocketError when trying to connect to: " + self._server_list[i][0]
						break
					#TODO: Add exception handling. 
					print "Connected to " + self._server_list[i][0] + "\n"
					connections.append(ftp)
					i=i+1
					return connections
		 
	def list(self):
		"""Sends list command to all connected servers and outputs in sys.out"""
		connections = self.connect()
		if connections:
			for con in connections:
				con.retrlines('LIST')
		else:
			print "No connections"

class ConnectionInfo():
	"""Class that stores information about the FTP connection"""
	def __init__(self, url, username, password, port=21):
		self.url = url
		self.port = port
		self.username = username
		self.password = password

class ServerList():
	def make_array(self):
		server_list = open("serverlist.txt", "r")
		server_list_lines = sum(1 for line in server_list.readlines())
		server_list_array = [ [ 0 for i in range(4) ] for j in range(server_list_lines) ]
		server_list.seek(0)

		for i in range(server_list_lines):
			server_list_array[i] = server_list.readline().rstrip("\n").split(",")
		server_list.close()

		return server_list_array
