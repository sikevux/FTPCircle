#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-
# vim:fileencoding=utf8

#Import all the moudles that should be in the README file.
import Main
import sys
import Database

#TODO: Write to file (only delete the last part of the file)
#TODO: Better markup
#TODO: Do not include modules/classes that is imported from standard library
#TODO: Fix better Try, Except
class CommentGenerate:
	def __init__(self):
		newfile = self.openFile()
		for row in self.generateComments(): 
			print(row)
			newfile.append(row)
		self.writeToFile(newfile)
		
	
	def generateComments(self):
		array = []
		for name in dir(Main):
			info = getattr(Main, name).__doc__
			if info != None:
				array.append("###" +name + " \n" + info + "\n")
		
		for name in dir(Database):
			info = getattr(Database, name).__doc__
			if info != None:
				array.append("###" +name + " \n" + info + "\n")
			
		return array
		

	def openFile(self):
		try:
			file = open("README.md", "r")
			newfile = []
			i = 0
			for row in file: 
			
				newfile.append(row[:-1])
				i += 1
				if row == "Main functions\n":
					newfile.append("--------------\n")
					break
		except IOError:
			print("Could not open README.md")
			sys.exit

			file.close()

		return newfile

		
	def writeToFile(self, newfile):
		try:
			file = open("README.md", "w")
			for row in newfile:
				print(row, file=file)
		except IOError:
			print("Could not write to README.md")
		file.close()
