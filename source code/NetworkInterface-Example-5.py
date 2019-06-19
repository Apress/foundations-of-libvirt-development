# Example-5.py
from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)

ifaceNames = conn.listInterfaces()

print("Active host interfaces:")
for ifaceName in ifaceNames:
    print('  '+ifaceName)

conn.close()
exit(0)
