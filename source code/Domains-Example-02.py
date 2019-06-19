# Example-2.py
from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)

domainName = 'someguest'
dom = conn.lookupByName(domainName)
if dom == None:
    print('Failed to get the domain object', file=sys.stderr)

conn.close()
