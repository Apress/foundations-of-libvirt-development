# Example-13.py
from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)

iface = conn.interfaceLookupByName('eth2')

# get the interface xml description
xml = iface XMLDesc(0)
# destroy the interface
iface.destroy(0)

# do what you need while the interface is down

# now bring the interface back up
iface = conn.interfaceDefineXML(xml, 0)
# activate the interface
iface.create(0)

conn.close()
exit(0)
