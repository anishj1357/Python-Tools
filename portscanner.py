#!/usr/bin/python3

from socket import *
import optparse
from threading import *

def connScan(tar_Host,tar_Port):
	try:
		sock = socket(AF_INET,SOCK_STREAM)
		sock.connect((tar_Host,tar_Port))
		print("[+] {} TCP port is Open".format(tar_Port))
	except:
		print("[-] {} TCP port closed".format(tar_Port))
	finally:
		sock.close()


def portScanner(tar_Host,tar_Ports):
	try:
		tar_IP = gethostbyname(tar_Host)
	except:
		print("Unknown Host {}".format(tar_Host))
	try:
		tar_name = gethostbyaddr(tar_Host)
		print("[+] Scan Results for {} ".format(tar_name[0]))
	except:
		print("[+] Scan Results for {} ".format(tar_IP))
	setdefaulttimeout(10)
	for tar_Port in tar_Ports:
		t = Thread(target = connScan, args =(tar_Host, int(tar_Port)))
		t.start()


def main():
	parser = optparse.OptionParser('Usage of the scanner: ' + '-H <target Host> -p <target Port>')
	parser.add_option('-H', dest = 'tar_Host', type = 'string', help = 'Specify the Target Host')
	parser.add_option('-p', dest = 'tar_Port', type = 'string', help = 'Specify the Target Ports seperated by comma')
	(options, args) = parser.parse_args()
	tar_Host = options.tar_Host
	tar_Ports = str(options.tar_Port).split(",")
	if (tar_Host == None) | (tar_Ports == None):
		print(parser.usage)
		exit(0)

	portScanner(tar_Host,tar_Ports)


if __name__ == '__main__':
	main()
