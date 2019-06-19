# Example-12.py
from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)

iface = conn.interfaceLookupByName('br0')

# get the xml prior to undefining the interface
xml = iface.XMLDesc(0)
# now undefine the interface
iface.undefine()
# the interface is now undefined and the iface variable 
#     is no longer be usable

conn.close()
exit(0)
