import subprocess
import sys

class CommandAction:
	name = "command"
	def __init__(self,handler,command):
		self.command = command
	def run(self):
		try:
			subprocess.Popen("C:\Windows\System32\cmd.exe /c "\
			+self.command.replace("%1",sys.argv[3]),shell=True)
		except:
			subprocess.Popen("C:\Windows\System32\cmd.exe /c "\
			+self.command,shell=True)
		
exports = [CommandAction]