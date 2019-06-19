# Example-31.py
from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)

models = conn.getCPUModelNames('x86_64')

for model in models:
    print(model)

conn.close()
exit(0)
