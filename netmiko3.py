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
routing = [
            'router ospf 100',
            'net 192.168.1.0 0.0.0.255 area 0',
            'net 192.168.2.0 0.0.0.255 area 0',
            'net 10.10.10.0 0.0.0.255 area 0',
            'net 1.1.1.1 0.0.0.0 area 0'
]
print(conn.send_config_set(routing))

#konfig router 1
conn = ConnectHandler(**router1)
#privilege exec mode
print(conn.enable())

#global config mode
routing = [
            'router ospf 100',
            'net 192.168.1.0 0.0.0.255 area 0',
            'net 192.168.3.0 0.0.0.255 area 0',
            'net 20.20.20.0 0.0.0.255 area 0',
            'net 10.10.10.0 0.0.0.255 area 0',
            'net 2.2.2.2 0.0.0.0 area 0'
]
print(conn.send_config_set(routing))

#konfig router 2
conn = ConnectHandler(**router2)
#privilege exec mode
print(conn.enable())

#global config mode
routing = [
            'router ospf 100',
            'net 192.168.1.0 0.0.0.255 area 0',
            'net 192.168.4.0 0.0.0.255 area 0',
            'net 20.20.20.0 0.0.0.255 area 0',
            'net 3.3.3.3 0.0.0.0 area 0'
]
print(conn.send_config_set(routing))
print(conn.send_command('sh ip ro'))
