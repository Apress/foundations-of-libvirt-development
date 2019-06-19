# Example-10.py
from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)

iface = conn.interfaceLookupByName('eth0')

print("The interface XML description is:\n"+iface.XMLDesc(0))

conn.close()
exit(0)
