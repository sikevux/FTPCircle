#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-
# vim:fileencoding=utf8

import unittest
from Main import FTPConnector, ConnectionInfo, ServerList, Main
import CommentGenerate
import Database

class TestSequence(unittest.TestCase):
	""" Class to do all the testing"""
	
	def setUp(self):
		""" Things that will need to be run before the tests"""
		self._server_list = ServerList("serverlist.csv")
		self._server_list_matrix = self._server_list.make_matrix()

	def test_connect(self):
		self._ftp_connector = FTPConnector(self._server_list_matrix)

	def test_list(self):
		self._ftp_connector = FTPConnector(self._server_list_matrix)
		self._ftp_connector.list()

	def test_discconect(self):
		self._ftp_connector = FTPConnector(self._server_list_matrix)
		self._ftp_connector.disconnect()
	def test_CommentGenerate(self):
		c = CommentGenerate.CommentGenerate()
		c.openFile()
	def test_Database(self):
		d = Database.Database()
		file_list= [["fil1", "/etc/fil1", "server.se"],["fil2", "/etc/fil2", "server.org"],["fil3", "/etc/fil3", "server.com"]]
		d.updateDB(file_list)
		print("------DATABASE DUMP ---------")
		d.list()
		d.disconnect()
		#d.initDB() #This is already done and the file is in the repo
#	def test_download(self):
#		self._ftp_connector = FTPConnector(self._server_list_matrix)
#		self._ftp_connector.download("README")
#		#d.initDB() #This is already done and the file is in the repo 
		
#	def test_Main(self):
#		main = Main()
		#main.list()

if __name__ == '__main__':
	unittest.main()
