#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""Old school testing"""
from Main import FTPConnector, ConnectionInfo, ServerList
m = ServerList()
slist = m.make_array()
t = FTPConnector(slist)
<<<<<<< HEAD
t.connect()
=======
t.list()
>>>>>>> upstream/master
""" t.list() is broken """
"""Soon to be unit testing class"""
