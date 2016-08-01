import os
import sys
import json
import binascii
import datetime 
import platform

def getTime():
	"""Return a readable time string

	Returns:
		string with time with format Hour:Minute:Second

	Notes about time: 
		- 'Readable' times use datetime and follow the format returned by this function
		- 'API' times use int(time.time())
		- Python unix time is in seconds, but Javascript and other languages use milliseconds
	"""
	return datetime.datetime.now().strftime('%H:%M:%S')


def getDate():
	"""Return a readable date string
	
	Returns:
		string with default date format YYYY-MM-DD
	"""
	return str(datetime.datetime.now().date())


def toJson(val):
	"""Return JSON string

	Supported datatypes:
		<class 'sqlalchemy.engine.result.RowProxy'>
		<type 'dict'>

	Args:
		val: datatype that gets converted to JSON string
	"""
	if str(type(val)) == "<class 'sqlalchemy.engine.result.RowProxy'>":
		return json.dumps(dict(val.items()))
	return json.dumps(val)


def randomString(length=16):
	"""Return a randomly generated string
	
	Args:
		length: integer for the length of the string divided by 2

	Returns:
		string thats randomly generated given a length
	"""
	return binascii.hexlify(os.urandom(length))


def getErrorLineNumber():
	"""Return line number of error

	This is useful if you're using 'try: except Exception as e:'

	Returns:
		integer of the line number where the error occurred
	"""
	exc_type, exc_obj, exc_tb = sys.exc_info()
	return exc_tb.tb_lineno

def say(msg):
	"""Read a message through the speakers

	Darwin systems only

	Args:
		msg: string that will be read aloud
	"""
	if platform.system() == 'Darwin':
		os.system("say %s" %(msg))


class Logger():
	"""Class for logging
	
	Args:
		currentWorkingDirectory: string in reference to your Current Working Directory, ie. os.path.dirname(os.path.abspath(__file__))
		scriptLogDescription: string in reference to the name of your script, ie. 'AS' (for script api_server.py)
		enableLogging: boolean to enable logging to stdout
	"""
	def __init__(self, scriptLogDescription, currentWorkingDirectory, enableLogging=True, toFile=False):
		self.currentWorkingDirectory = currentWorkingDirectory
		self.scriptLogDescription = scriptLogDescription
		self.enableLogging = enableLogging
		self.toFile = toFile
	
	def log(self, msg, toFile='ignore'):
		"""Print some text with a readable timestamp

		Args:
			msg: string to print
			toFile: boolean to write to log file in same directory
		"""
		line = '[%s] %s: %s' %(getTime(), self.scriptLogDescription, msg)
		if self.enableLogging:
			print line
		_toFile = toFile if toFile != 'ignore' else self.toFile
		if _toFile:
			try: os.mkdir('%s/logs' %(self.currentWorkingDirectory))
			except: pass
			fp = '%s/logs/%s.log' %(self.currentWorkingDirectory, self.scriptLogDescription) 
			with open(fp, 'a') as f:
				f.write(line)
				f.write('\r\n')
			fp = '%s/logs/main.log' %(self.currentWorkingDirectory) 
			with open(fp, 'a') as f:
				f.write(line)
				f.write('\r\n')


if __name__ == '__main__':
	CWD = os.path.dirname(os.path.abspath(__file__))
	l = Logger("TEST", CWD)
	l.log("testing 123")

	print toJson({})
	print randomString(10)
	print getTime()
	print getDate()
	say("hello")

	try: raise
	except Exception as e: print getErrorLineNumber()