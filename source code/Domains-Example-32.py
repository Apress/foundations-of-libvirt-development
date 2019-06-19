# Example-32.py
from __future__ import print_function
import sys
import libvirt
from xml.etree import ElementTree

domName = 'Fedora22-x86_64-1'

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)

dom = conn.lookupByID(5)
if dom == None:
    print('Failed to find the domain '+domName, file=sys.stderr)
    exit(1)

tree = ElementTree.fromstring(dom.XMLDesc())
iface = tree.find('devices/interface/target').get('dev')
stats = dom.interfaceStats(iface)
print('read bytes:    '+str(stats[0]))
print('read packets:  '+str(stats[1]))
print('read errors:   '+str(stats[2]))
print('read drops:    '+str(stats[3]))
print('write bytes:   '+str(stats[4]))
print('write packets: '+str(stats[5]))
print('write errors:  '+str(stats[6]))
print('write drops:   '+str(stats[7]))

conn.close()
exit(0)
