# Example-23.py
from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)

mem = conn.getFreeMemory()

print("Free memory on the node (host) is " + str(mem) + " bytes.")

conn.close()
exit(0)
