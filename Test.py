#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# vim:fileencoding=utf8

import unittest
from Main import FTPConnector, ConnectionInfo, ServerList

class TestSequence(unittest.TestCase):
	""" Class to do all the testing"""
	def setUp(self):
		""" Things that will need to be run before the tests"""
		self._server_list = ServerList()
		self._server_list_array = self._server_list.make_array()

	def test_connect(self):
		self._ftp_connector = FTPConnector(self._server_list_array)

	def test_list(self):
		self._ftp_connector = FTPConnector(self._server_list_array)
		self._ftp_connector.list()

	def test_discconect(self):
		self._ftp_connector = FTPConnector(self._server_list_array)
		self._ftp_connector.disconnect()

if __name__ == '__main__':
	unittest.main()
