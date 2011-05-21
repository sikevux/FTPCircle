#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# vim:fileencoding=utf8

import unittest
from Main import FTPConnector, ConnectionInfo, ServerList
import CommentGenerate

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

if __name__ == '__main__':
	unittest.main()
