from ftplib import FTP
from ftplib import FTP_TLS

class FTPConnector():
	""" Class that connects to the FTP servers and takes care of interfaceing with the FTP"""
	_connected = False
	_server_list = []
	
	def __init__(self, server_list):
		self._server_list = server_list

	def connect(self):
		"""Connects to all of the servers listed in _server_lsit"""
		if self._connected:
			print "Already connected"
			return None 
			#TODO: Save connection instances. 
		else:
			print "Not connected.\n"
			print "Connnecting... \n"
			connections = []
			if len(self._server_list) == 0 :
				print "No servers where specified. \n"
			else:
				for server in self._server_list:
					if server.url.startswith( 'ftpes' ):
						ftp = FTP_TLS(server.url, server.username, server.password)
						# Now one could specify crt and key file but meh.
					else:				
						ftp = FTP(server.url, server.username, server.password)
					#TODO: Add exception handling. 
					print "Connected to " + server.url "\n"
					connections.append(ftp)
					return connections
		 
	def list(self):
		"""Sends list command to all connected servers and outputs in sys.out"""
		connections = self.connect()
		for con in connections:
			con.retrlines('LIST') 


			
			
class ConnectionInfo():
	"""Class that stores information about the FTP connection"""
	def __init__(self, url, username, password, port=21):
		self.url = url
		self.port = port
		self.username = username
		self.password = password
