# Example-9.py
from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)

host = conn.getHostname()
print('Hostname:'+host)

conn.close()
exit(0)
