# Example-5.py
from __future__ import print_function
import sys
import libvirt

conn1 = libvirt.open('qemu:///system')
if conn1 == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)
conn2 = libvirt.open('qemu:///system')
if conn2 == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)
conn1.close()
conn2.close()
exit(0)
