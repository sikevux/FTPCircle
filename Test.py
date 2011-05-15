#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""Old school testing"""
from Main import FTPConnector, ConnectionInfo
slist = [ConnectionInfo("192.168.1.100", "dummy", "server")]
t = FTPConnector(slist)
t.list()

"""Soon to be unit testing class"""
