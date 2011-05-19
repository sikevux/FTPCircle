#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# vim:fileencoding=utf8

# http://docs.python.org/library/sqlite3.html
import sqlite3
class Database():
	"""Interface to the SQLite database. This is the class that will cache the servers filenames and also conduct searches."""
	def __init__(self):
		self.conn = sqlite3.connect('database.db')
		self.c = self.conn.cursor()
	
	def connect(self):
		"""Connects to the database"""
		#
	def search(self, search_string):
		"""Seaches the databse after the input search_string. 
		Returns a list of strings with possible results"""
		#
	def updateDB(self, file_list):
		"""Clears the database and adds the files from file_list. 
		(We need a good way to pass this information from the FTP class. A matrix of strings?)"""
		#
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