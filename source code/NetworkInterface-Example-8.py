# Example-8.py
from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)

iface = conn.interfaceLookupByMACString('00:01:02:03:04:05')

print("The interface name is: "+iface.name())

conn.close()
exit(0)
