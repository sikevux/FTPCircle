#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-
# vim:fileencoding=utf8

from ftplib import FTP
from ftplib import FTP_TLS
import socket
from threading import Thread
from threading import RLock
from re import search
import Database

class Main():
	"""Main class, connecting FTPConnector and Database, 
	takes care of UI input.
	To clearify: UI CALLS THIS CLASS WHICH WRAPPS THE WHOLE PROGRAM AND HELPS OTHER CLASSES TO INTERFACE WITH EACH OTHER (yay, caps.)"""
	
	def __init__(self):
		self.serverlist = ServerList().make_matrix()
		self.connector = FTPConnector(self.serverlist) 
		self.database = Database.Database()
		self.connector.connect()
		self.update()
		self.list()

	def update(self):
		"""Not completed. Gets file lists from all FTP servers. Parses the info and writes them to the database"""
		print("-----UPDATE------")
		filelist = self.connector.list()
		db=[]
		for servers in filelist:
			for row in servers:
				part = row.split()
				add = []
				add.append(part[8]) #filename
				add.append("not set") #Fullpath	
				add.append(	"not set") #hostname / ip
				db.append(add)
		self.database.updateDB(db)
		
	def get(self, id):
		'''Downloads file with id-number id'''
		pass
	def list(self, location="/"):
		'''Return list of all the files, used by UI'''
		self.database.list()
		pass
		
class FTPThread(Thread):
	""" Class to do the threaded fetching """
	ftp = None
	def __init__(self, url, user, password, tls):
		Thread.__init__(self)
		self.url = url
		self.user = user
		self.password = password
		self.tls = tls
		#Get thread lock to enable synchronized methods.
		self._lock = RLock()

	def run(self):
		"""Connects to the FTP and creates FTP object stored in self.ftp"""
		self._lock.acquire()
		try:
			if self.tls == 1:
				self.ftp = FTP_TLS(self.url, self.user, self.password)
			else:
				self.ftp = FTP(self.url, self.user, self.password)
		except socket.error as msg:
			print("SocketError when trying to connect to: " + self.url)
		self._lock.release()
	
	def list(self):
		"""Sends list command to self.ftp and outputs it in std.out"""
		self._lock.acquire()
		if self.ftp == None:
			print("No connection")
		else:	
			self.lines = []  
			#self.lines = self.ftp.nlst()
			self.ftp.retrlines('LIST', self.lines.append) 
			return self.lines
		self._lock.release()

	def download(self, filename, outputFile):
		"""Downloads file from server in binary mode"""
		self._lock.acquire()
		if self.ftp is None:
			print("No connection")
		else:
			try:
				outputFile
			except NomeError:
				outputFile = None

			if outputFile is None:
				outputFile = sys.stdout

			self.ftp.retrbinary("RETR " + filename, outputFile.write)
		self._lock.release()

	def disconnect(self):
		"""Disconnects the connection to the FTP server"""
		self._lock.acquire()
		if self.ftp != None:
			if not self.ftp.quit():
				self.ftp.close()
		else:
			print("Nothing to disconnect")
		self._lock.release()

class FTPConnector():
	""" Class that connects to the FTP servers and takes care of interfaceing with the FTP"""
	_connected = False
	_server_list = []

	def __init__(self, server_list):
		self._server_list = server_list

	def connect(self):
		"""Connects to all of the servers listed in _server_list"""
		if self._connected:
			print("Already connected")
			return None 
			#TODO: Save connection instances. (Already done in the threads, need check if Timeout has set in)
		else:
			print("Connnecting... \n")
			connections = []
			if len(self._server_list) == 0 :
				print("No servers where specified. Please verify serverlist.csv is not empty \n")
			else:
				i=0
				for line in self._server_list:
					try:
						if self._server_list[i][0] != '':
							if self._server_list[i][3] == 1:
								ftp = FTPThread(self._server_list[i][0], self._server_list[i][1], self._server_list[i][2], 1)
								ftp.start()
							else:
								ftp = FTPThread(self._server_list[i][0], self._server_list[i][1], self._server_list[i][2], 0)
								ftp.start()
						else:
							break

					except:
						print("Something went wrong trying to connect to: " + self._server_list[i][0])
					#TODO: Add better exception handling. 
					print("Connected to " + self._server_list[i][0] + "\n")
					connections.append(ftp)
					i += 1

				return connections
		 
	def list(self):
		"""Sends list command to all servers listed in serverlist.csv and outputs in sys.out"""
		connections = self.connect()
		files= []
		if connections:
			for con in connections:
				files.append(con.list())
			return files
		else:
			print("No connections")

	def disconnect(self):
		"""Disconnects all connections"""
		connections = self.connect()
		if connections:
			for con in connections:
				con.disconnect()
		else:
			print("No connections")

class ConnectionInfo():
	"""Class that stores information about the FTP connection"""
	def __init__(self, url, username, password, port=21):
		self.url = url
		self.port = port
		self.username = username
		self.password = password

class ServerList():
	"""Interface to serverlist.csv """

	def __init__(self, server_list):
		self._server_list = server_list
	def make_matrix(self):
		"""Parse serverlist.csv and generates a matrix representing the information """
		try:
			server_list = open(self._server_list, "r")
		except IOError:
			print("File not found:", self._server_list)
			sys.exit()

		server_list_lines = sum(1 for line in server_list.readlines())
		server_list_matrix = [ [ 0 for i in range(4) ] for j in range(server_list_lines) ]
		server_list.seek(0)

		for i in range(server_list_lines):
			server_list_matrix[i] = server_list.readline().rstrip("\n").split(",")
		server_list.close()

		return server_list_matrix
