# scipt conenct network automation to single switch
import telnetlib
import getpass

host = input("Masukan Ip Router : ")
user = input("Masukan username router : ")
password = getpass.getpass("Masukan Password : ")

tn = telnetlib.Telnet(host)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")      #untuk melakukan encode nilai pada variabel user.
                                            #bedanya python3 dengan python2 text harus di encode dulu
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")

tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")
tn.write(b"conf t\n")
tn.write(b"vlan 100\n")
tn.write(b"name vlan100\n")
tn.write(b"end\n")
tn.write(b"exit\n")
print(tn.read_all().decode('ascii')) #untuk menampilkans semua teks dan mencetak konfigurasi

# scipt conenct network automation to single switch
import telnetlib
import getpass

host = input("Masukan Ip Router : ")
user = input("Masukan username router : ")
password = getpass.getpass("Masukan Password : ")

tn = telnetlib.Telnet(host)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")      #untuk melakukan encode nilai pada variabel user.
                                            #bedanya python3 dengan python2 text harus di encode dulu
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"conf t\n")
tn.write(b"int lo1\n")
tn.write(b"ip add 11.11.11.11 255.255.255.0\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
