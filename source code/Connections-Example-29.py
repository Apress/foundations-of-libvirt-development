# Example-29.py
from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)

map = conn.getCPUMap()

print("CPUs: " + str(map[0]))
print("Available: " + str(map[1]))

conn.close()
exit(0)
