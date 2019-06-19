# Example-11.py
from __future__ import print_function
import sys
import libvirt

xml = """"
<interface type='ethernet' name='eth0'>
  <start mode='onboot'/>
  <mac address='aa:bb:cc:dd:ee:ff'/>
  <protocol family='ipv4'>
    <ip address="192.168.0.5" prefix="24"/>
    <route gateway="192.168.0.1"/>
  </protocol>
</interface>"""

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to create the interface eth0', \
          file=sys.stderr)
    exit(1)

# create/modify a network interface
iface = conn.interfaceDefineXML(xml, 0)
# activate the interface
iface.create(0)

print("The interface name is: "+iface.name())

conn.close()
exit(0)
