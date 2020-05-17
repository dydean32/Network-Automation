#koneksi ke multi switch (vlan configuration)
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

    tn.write(b"enable\n")

    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

    tn.write(b"conf t\n")
    tn.write("vlan 100")
    tn.write("name vlan100")
    tn.write("vlan 200")
    tn.write("name vlan200")
    tn.write("vlan 300")
    tn.write("name vlan300")
    tn.write(b"end\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))
