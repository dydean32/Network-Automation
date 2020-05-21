import paramiko
import getpass
import time

user = raw_input("Masukan Username : ")
passwd = getpass.getpass("Masukan Password : ")
ip_file = open("ip.txt","r")
iplist = ip_file.readlines()

for host in iplist:
  ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=host,username=user,password=passwd)

	conn = ssh_client.invoke_shell()

  conn.send("enable\n")
	conn.send("conf t\n")
  if host == '192.168.1.2\n':
        conn.send("router eigrp 10\n")
        conn.send("network 192.168.1.0\n")
        conn.send("network 10.10.10.0\n")
        conn.send("network 192.168.2.0\n")
  elif host == '192.168.1.3\n':
        conn.send("router eigrp 10\n")
        conn.send("network 192.168.1.0\n")
        conn.send("network 10.10.10.0\n")
        conn.send("network 20.20.20.0\n")
        conn.send("network 192.168.3.0\n")
  elif host == '192.168.1.4\n':
        conn.send("router eigrp 10\n")
        conn.send("network 192.168.1.0\n")
        conn.send("network 20.20.20.0\n")
        conn.send("network 192.168.4.0\n")
  conn.send("end\n")
  conn.send("wr\n")
    
  time.sleep(2)

	output = conn.recv(65535)
	print(output.decode("ascii"))

