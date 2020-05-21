import paramiko
import getpass
import time

user = raw_input("Masukan Username : ")
passwd = getpass.getpass("Masukan Password : ")
ip_file = open("ip.txt","r")
iplist = ip_file.readlines()


n = 1
o = 10
p = 20

for host in iplist:
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=host,username=user,password=passwd)

	conn = ssh_client.invoke_shell()

	conn.send("enable\n")
	conn.send("conf t\n")
	conn.send("int lo 0\n")
	conn.send("ip add {}.{}.{}.{} 255.255.255.255\n".format(n,n,n,n))
	conn.send("no sh\n")
    if host == '192.168.1.2\n':
        conn.send("int g2/0\n")
        conn.send("ip add {}.{}.{}.{} 255.255.255.0\n".format(o,o,o,n))
        conn.send("no sh\n")
        conn.send("int g4/0\n")
        conn.send("ip add 192.168.2.1 255.255.255.0\n")
        conn.send("no sh\n")
    elif host == '192.168.1.3\n':
        conn.send("int g2/0\n")
        conn.send("ip add {}.{}.{}.{} 255.255.255.0\n".format(o,o,o,n))
        conn.send("no sh\n")
        conn.send("int g3/0\n")
        conn.send("ip add {}.{}.{}.{} 255.255.255.0\n".format(p,p,p,n))
        conn.send("no sh\n")
        conn.send("int g4/0\n")
        conn.send("ip add 192.168.3.1 255.255.255.0\n")
        conn.send("no sh\n")
    elif host == '192.168.1.4\n':
        conn.send("int g3/0\n")
        conn.send("ip add {}.{}.{}.{} 255.255.255.0\n".format(p,p,p,n))
        conn.send("no sh\n")
        conn.send("int g4/0\n")
        conn.send("ip add 192.168.4.1 255.255.255.0\n")
        conn.send("no sh\n")

	time.sleep(2)

	output = conn.recv(65535)
	print(output.decode("ascii"))

	ssh_client.close()

	n = n + 1
