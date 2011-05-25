#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-
# vim:fileencoding=utf8

# http://docs.python.org/library/sqlite3.html
import sqlite3
class Database():
	"""Interface to the SQLite database. This is the class that will cache the servers filenames and also conduct searches."""
	#TODO: Fix Try Except
	def __init__(self):
		self.conn = sqlite3.connect('database.db')
		self.c = self.conn.cursor()
	
	def disconnect(self):
		"""Closes all the database connections"""
		self.c.close()
		self.conn.close()
		#
	def search(self, search_string):
		"""Seaches the databse after the input search_string. 
		Returns a list of strings with possible results"""
		#
	def _clearTables(self):
		"""Private method, clears data from table"""
		command = "DELETE FROM filelist;"
		self.c.execute(command)
		self.conn.commit()
		
	def updateDB(self, file_list):
		"""Clears the database and adds the files from file_list. 
		(We need a good way to pass this information from the FTP class. A matrix of strings?)"""
		self._clearTables()
		for i in range(len(file_list)):
			self.c.execute("insert into filelist (filename, full_file_path, server) values ('" + file_list[i][0] + "','" + file_list[i][1] + "','"+ file_list[i][2] + "'); ")
		#self.c.execute(command)
		self.conn.commit()
	def getInfo(self, index):
		"""Returns the information stored on line nbr index. Allowing the interface to show human readable information."""
		#
	def list(self, location="/"):
		"""Returns a list of strings with the file information from a certain folder (root if not specified)"""
		
		#
	def treeList(self, location="/"):
		"""Returns a tree view of the filesystems. Reqursive from the starting point specified in location (root folder is default). """
	
	def initDB(self):
		"""Initiates and creates the database with columns"""
		command = """
CREATE TABLE 'filelist'('id' INTEGER PRIMARY KEY ASC, 'filename' VARCHAR(100), 'full_file_path' VARCHAR(200), 'server' VARCHAR(100));
"""
		self.c.execute(command)
		conn.commit()
