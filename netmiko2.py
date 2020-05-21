from netmiko import ConnectHandler
router = {
    'device_type':'cisco_ios',
    'ip':'192.168.1.2',
    'username':'cisco',
    'password':'cisco'
}
router1 = {
    'device_type':'cisco_ios',
    'ip':'192.168.1.3',
    'username':'cisco',
    'password':'cisco'
}
router2 = {
    'device_type':'cisco_ios',
    'ip':'192.168.1.4',
    'username':'cisco',
    'password':'cisco'
}
#konfig router 1
conn = ConnectHandler(**router)
#privilege exec mode
print(conn.enable())

#global config mode
inter = [
        'interface loopback 1',
        'ip address 1.1.1.1 255.255.255.255',
        'no shutdown',
        'interface g2/0',
        'ip address 10.10.10.1 255.255.255.0',
        'no shutdown',
        'interface g3/0',
        'ip address 192.168.2.1 255.255.255.0',
        'no shutdown'
]
print(conn.send_config_set(inter))
print(conn.send_command('sh ip int b'))

#konfig router 1
conn = ConnectHandler(**router1)
#privilege exec mode
print(conn.enable())

#global config mode
inter = [
        'interface loopback 1',
        'ip address 2.2.2.2 255.255.255.255',
        'no shutdown',
        'interface g2/0',
        'ip address 10.10.10.2 255.255.255.0',
        'no shutdown',
        'interface g3/0',
        'ip address 20.20.20.1 255.255.255.0',
        'no shutdown',
        'interface g4/0',
        'ip address 192.168.3.1 255.255.255.0',
        'no shutdown'
]
print(conn.send_config_set(inter))
print(conn.send_command('sh ip int b'))


#konfig router 2
conn = ConnectHandler(**router2)
#privilege exec mode
print(conn.enable())

#global config mode
inter = [
        'interface loopback 1',
        'ip address 3.3.3.3 255.255.255.255',
        'no shutdown',
        'interface g2/0',
        'ip address 20.20.20.2 255.255.255.0',
        'no shutdown',
        'interface g3/0',
        'ip address 192.168.4.1 255.255.255.0',
        'no shutdown'
]
print(conn.send_config_set(inter))
print(conn.send_command('sh ip int b'))
