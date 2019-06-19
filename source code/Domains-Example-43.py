# Example-43.py
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

id = dom.ID()
if id == -1:
    print('The domain is not running so has no ID.')
else:
    print('The ID of the domain is ' + str(id))

conn.close()
exit(0)
