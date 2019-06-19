# Example-27.py
from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)

model = conn.getSecurityModel()

print(model[0] + " " + model[1])

conn.close()
exit(0)
