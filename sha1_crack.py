#!/usr/bin/python3

from urllib.request import urlopen
import hashlib
from termcolor import colored


sha1_hash = input("Enter the SHA-1 Hash value: ")

pass_list = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt').read(), 'utf-8')

for i in pass_list.split("\n"):
	hash_guess = hashlib.sha1(bytes(i,'utf-8')).hexdigest()
	if hash_guess == sha1_hash:
		print(colored("[+] Password found : " +str(i),'green'))
		quit()
	else:
		print(colored("[-] " + str(i) + " is not the password. Trying next password from the list",'red'))
print(colored("[-]Password not found in the list",'red'))
