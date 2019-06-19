# Example-53.py
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

mem = dom.maxMemory()
if mem > 0:
    print('The max memory for domain is ' + str(mem) + 'MB')
else:
    print('There was an error.')

conn.close()
exit(0)
