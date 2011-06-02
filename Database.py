#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-
# vim:fileencoding=utf8

# http://docs.python.org/library/sqlite3.html
import sqlite3
class Database():
	"""Interface to the SQLite database. This is the class that will cache the servers filenames and also conduct searches.
		SQLite escapes are handled by the python SQL interface."""
	def __init__(self):
		self.conn = sqlite3.connect('database.db')
		self.c = self.conn.cursor()
		
	def initDB(self):
		"""Initiates and creates the database with columns"""
		command = """
CREATE TABLE 'filelist'('id' INTEGER PRIMARY KEY ASC, 'filename' VARCHAR(100), 'full_file_path' VARCHAR(200), 'server' VARCHAR(100));
"""
		self.c.execute(command)
		conn.commit()
	
	def disconnect(self):
		"""Closes all the database connections"""
		self.c.close()
		self.conn.close()
		
	def _clearTables(self):
		"""Private method, clears data from table"""
		command = "DELETE FROM filelist;"
		self.c.execute(command)
		self.conn.commit()
		
	def updateDB(self, file_list):
		"""Clears the database and adds the files from file_list. 
		file_list[i][j] where i is the row and 
		j=0 Name
		j=1 Full file path
		j=2 server adress/ip
		(This needs nicer syntax)"""
		self._clearTables()
		for i in range(len(file_list)):
			self.c.execute("INSERT INTO filelist (filename, full_file_path, server) values ('" + file_list[i][0] + "','" + file_list[i][1] + "','"+ file_list[i][2] + "'); ")
		self.conn.commit()
		
	def getInfo(self, index):
		"""Returns the information stored on line nbr index. Allowing the interface to show human readable information."""
		#
		
	def list(self, location="/"):
		"""Returns a list of strings with the file information from a certain folder (root if not specified)"""
		#
		self.c.execute('select * from filelist')
		for row in self.c:
			print(row)
		
		
	def treeList(self, location="/"):
		"""Returns a tree view of the filesystems. Reqursive from the starting point specified in location (root folder is default). """
	
	def initDB(self):
		"""Initiates and creates the database with columns"""
		command = """
CREATE TABLE 'filelist'('id' INTEGER PRIMARY KEY ASC, 'filename' VARCHAR(100), 'full_file_path' VARCHAR(200), 'server' VARCHAR(100));
"""
		self.c.execute(command)
		conn.commit()
		#
		
	def search(self, search_string):
		"""Seaches the databse after the input search_string. 
		Returns a list of strings with possible results"""
		#
