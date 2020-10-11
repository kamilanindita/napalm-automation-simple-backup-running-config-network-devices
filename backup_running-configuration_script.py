import napalm
from datetime import datetime

cisco_device_ip_list = ['192.168.100.101']
junos_device_ip_list = ['192.168.100.102']
arista_device_ip_list = ['192.168.100.103']

def filename(hostname, ip_add):
    now = datetime.now()
    date_time = now.strftime("%H:%M:%S-%m:%d:%Y")
    name='backup_'+hostname+'_'+ip_add+'_'+ str(date_time) +'.txt'
    return name

print('###################################START AUTOMATION####################################')
for ip_device in cisco_device_ip_list:
	print('Connecting to cisco device ip '+ str(ip_device))
	driver = napalm.get_network_driver('ios')
	device = driver(hostname=ip_device, username='cisco', password='cisco123')
	device.open()
	print('Backup running configuration...')
	host_name=device.get_facts()['hostname']
	run_config=device.get_config()['running']
	SAVE_FILE = open(filename(host_name, ip_device), 'w')
	SAVE_FILE.write(run_config)
	SAVE_FILE.close()
	print('Successfully backed up the running config.')
	device.close()
	print('-------------------------------------------------------------------------------')

print('#######################################################################################')

for ip_device in junos_device_ip_list:
	print('Connecting to junos device ip '+ str(ip_device))
	driver = napalm.get_network_driver('junos')
	device = driver(hostname=ip_device, username='root', password='root123')
	device.open()
	print('Backup running configuration...')
	host_name=device.get_facts()['hostname']
	run_config=device.get_config()['running']
	SAVE_FILE = open(filename(host_name, ip_device), 'w')
	SAVE_FILE.write(run_config)
	SAVE_FILE.close()
	print('Successfully backed up the running config.')
	device.close()
	print('--------------------------------------------------------------------------------')

#print('########################################################################################')

for ip_device in arista_device_ip_list:
	print('Connecting to arista device ip '+ str(ip_device))
	driver = napalm.get_network_driver('eos')
	device = driver(hostname=ip_device, username='admin', password='admin123')
	device.open()
	print('Backup running configuration...')
	host_name=device.get_facts()['hostname']
	run_config=device.get_config()['running']
	SAVE_FILE = open(filename(host_name, ip_device), 'w')
	SAVE_FILE.write(run_config)
	SAVE_FILE.close()
	print('Successfully backed up the running config.')
	device.close()
	print('--------------------------------------------------------------------------------')


print('###########################################END##########################################')
