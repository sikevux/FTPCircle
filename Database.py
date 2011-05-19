#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# vim:fileencoding=utf8

# http://docs.python.org/library/sqlite3.html
import sqlite3
class Database():
	def __init__(self):
		self.conn = sqlite3.connect('files.db')
		self.c = self.conn.cursor()
	
	def connect(self):
		#
	def search(self, search_string):
		#
	def updateDB(self, file_list):
		#
	def getInfo(self, index):
		#
	def list(self, location="/")
		#