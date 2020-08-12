#!/usr/bin/python3

import subprocess

def change_mac_address(interface,mac):
	subprocess.call(['ifconfig',interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",mac])
	subprocess.call(['ifconfig',interface,"up"])

def main():
	interface = input("[*] Enter the interface which you want to change: ")
	new_mac_addr = input("Enter the MAC Address To Change To: ")
	before_mac_changed = subprocess.check_output(['ifconfig',interface])
	change_mac_address(interface,new_mac_addr)
	after_mac_change = subprocess.check_output(["ifconfig",interface])
	if before_mac_changed == after_mac_change:
		print("[-] Failed to change the mac address: " + new_mac_addr)
	else:
		print("[+] MAc Address has changed To: "+ new_mac_addr + " On " + interface)

main()
