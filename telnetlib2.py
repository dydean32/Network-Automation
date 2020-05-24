import telnetlib
import getpass

user = input("Masukan username router : ")
password = getpass.getpass("Masukan Password : ")

host = ['192.168.1.2','192.168.1.3','192.168.1.4']

for device_list in host:
    print("Konfigurasi ip {}: ".format(device_list))
    tn = telnetlib.Telnet(device_list)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")

    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"conf t\n")
    tn.write(b"int lo 100\n")
    if device_list == '192.168.1.2':
        tn.write(b"ip add 1.1.1.1 255.255.255.255\n") 
    elif device_list == '192.168.1.3':
        ip = "ip add 2.2.2.2 255.255.255.255"
        tn.write(ip.encode('ascii') + b"\n")#digunakan untuk menulis write jika ada string dan variable
    elif device_list == '192.168.1.4':
        ip = "ip add 3.3.3.3 255.255.255.255"
        tn.write(ip.encode('ascii') + b"\n")
    tn.write(b"no sh\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))
