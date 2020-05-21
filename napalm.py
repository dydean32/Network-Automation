from napalm import get_network_driver
import getpass

driver = get_network_driver('ios')
host = input("Masukan Ip Router : ")
user = input("Masukan username : ")
password =  getpass.getpass("Masukan Password : ")
device = driver(hostname=host,username=user,password=password)
device.open()

devshow = device.get_facts()
print(devshow)

device.close()
