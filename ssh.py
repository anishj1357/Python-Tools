
#!/usr/bin/python3
import pexpect

PROMPT = ['# ','>>> ','> ','\$ ']

def command_exec(child, command):
	child.sendline(command)
	child.expect(PROMPT)
	print(child.before)


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
	child.expect(PROMPT)
	return child


def main():
	host = input("Enter the host ip address: ")
	user = input("Enter the username: ")
	password = input("Enter the SSH password: ")
	child = connect(user,host,password)
	command = input("Enter the command to be executed:")
	command_exec(child, command)

main()

