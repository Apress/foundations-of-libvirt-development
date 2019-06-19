# Example-5.py
from __future__ import print_function
import sys
import libvirt
from xml.dom import minidom

poolName = 'default'

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)

sp = conn.storagePoolLookupByName(poolName)
if sp == None:
    print('Failed to find storage pool '+poolName, \
          file=sys.stderr)
    exit(1)

raw_xml = sp.XMLDesc(0)
xml = minidom.parseString(raw_xml)
name = xml.getElementsByTagName('name')
print('pool name: '+poolName)
spTypes = xml.getElementsByTagName('source')
for spType in spTypes:
    attr = spType.getAttribute('name')
    if attr != None:
        print('  name = '+attr)
    attr = spType.getAttribute('path')
    if attr != None:
        print('  path = '+attr)
    attr = spType.getAttribute('dir')
    if attr != None:
        print('  dir = '+attr)
    attr = spType.getAttribute('type')
    if attr != None:
        print('  type = '+attr)
    attr = spType.getAttribute('username')
    if attr != None:
        print('  username = '+attr)

conn.close()
exit(0)
