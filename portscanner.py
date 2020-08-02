#!/usr/bin/python3

from socket import *
import optparse
from threading import *

def connScan(tar_Host,tar_Port):
	try:
		sock = socket(AF_INET,SOCK_STREAM)
		sock.connect((tar_Host,tar_Port))
		banner = sock.recv(1024)
		print("[+]{}:{} running {}".format(tar_Host,tar_Port,banner))
	except:
		pass
	finally:
		sock.close()


def portScanner(tar_Host,tar_Ports):
	try:
		tar_IP = gethostbyname(tar_Host)
	except:
		print("Unknown Host {}".format(tar_Host))
	try:
		tar_name = gethostbyaddr(tar_Host)
	except:
		pass
	setdefaulttimeout(2)
	t = Thread(target = connScan, args =(tar_Host, int(tar_Ports)))
	t.start()


def main():
	parser = optparse.OptionParser('Usage of the scanner: ' + '-H <target Host> -p <target Port>')
	parser.add_option('-H', dest = 'tar_Host', type = 'string', help = 'Specify the Target Host')
	parser.add_option('-p', dest = 'tar_Port', type = 'string', help = 'Enter the port number till you want to scan')
	(options, args) = parser.parse_args()
	tar_Host = options.tar_Host
	tar_Ports = int(options.tar_Port)
	if (tar_Host == None) | (tar_Ports == None):
		print(parser.usage)
		exit(0)
	print("[+] Scan Results for {} ".format(tar_Host))
	for range_Ports in range(0,tar_Ports+1):
		portScanner(tar_Host,range_Ports)


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Thank you for using it")

