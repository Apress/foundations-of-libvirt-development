# Example-51.py
from __future__ import print_function
import sys
import libvirt
from xml.dom import minidom

domName = 'CentOS7'

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)

dom = conn.lookupByName(domName)
if dom == None:
    print('Failed to find the domain '+domName, file=sys.stderr)
    exit(1)

flag = dom.isActive()
if flag == True:
    print('The domain is active.')
else:
    print('The domain is not active.')

conn.close()
exit(0)
