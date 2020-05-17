#koneksi multi switch dgn pemanggilan file
import telnetlib
import getpass

user = input("Masukan username router : ")
password = getpass.getpass("Masukan Password : ")

ip_file = open("ip.txt","r")
iplist = ip_file.readlines()
for device_list in iplist:
    print("Konfigurasi ip {} ".format(device_list))
    tn = telnetlib.Telnet(device_list)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")

    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"enable\n")

    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

    tn.write(b"conf t\n")
    tn.write(b"int lo 200\n")
    if device_list == '192.168.1.2\n':
        ip = "ip add 10.10.10.10 255.255.255.255"
        tn.write(ip.encode('ascii') + b"\n")
    elif device_list == '192.168.1.3\n':
        ip = "ip add 20.20.20.20 255.255.255.255"
        tn.write(ip.encode('ascii') + b"\n")
    elif device_list == '192.168.1.4\n':
        ip = "ip add 30.30.30.30 255.255.255.255"
        tn.write(ip.encode('ascii') + b"\n")
    tn.write(b"no sh\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))
