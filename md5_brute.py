#!/usr/bin/python3

from urllib.request import urlopen
import hashlib
from termcolor import colored


md5_hash = input("Enter the MD5 Hash value: ")

pass_list = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt').read(), 'utf-8')

for i in pass_list.split("\n"):
	md5_guess = hashlib.md5(bytes(i,'utf-8')).hexdigest()
	if md5_guess == md5_hash:
		print(colored("[+] Password found : " +str(i),'green'))
		quit()
	else:
		print(colored("[-] " + str(i) + " is not the password. Trying next password from the list",'red'))
print(colored("[-]Password not found in the list",'red'))

