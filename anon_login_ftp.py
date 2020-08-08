#!/usr/bin/python3

import ftplib

def anonLogin(hostname):
	try:
		ftp = ftplib.FTP(hostname)
		ftp.login("anonymous","anonymous")
		print("[+] "+hostname +" FTP anonymous login successfull")
		return True
	except:
		print("[-] " +hostname +"FTP anonymous login Failed")

host = input("Enter the host ip address: ")
anonLogin(host)

