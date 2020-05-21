from netmiko import ConnectHandler

router = {
    'device_type':'cisco_ios',
    'ip':'192.168.1.2',
    'username':'cisco',
    'password':'cisco'
}
conn = ConnectHandler(**router)
#privilege exec mode
print(conn.enable())

#global config mode
cmd = [
        'interface loopback 1',
        'ip address 100.100.100.1 255.255.255.0',
        'no shutdown'
]
print(conn.send_config_set(cmd))
print(conn.send_command('sh ip int b'))
