# Example-39.py
from __future__ import print_function
import sys
import libvirt
from xml.dom import minidom

domName = 'Fedora22-x86_64-1'

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)

dom = conn.lookupByID(1)
if dom == None:
    print('Failed to find the domain '+domName, file=sys.stderr)
    exit(1)

raw_xml = dom.XMLDesc(0)
xml = minidom.parseString(raw_xml)
diskTypes = xml.getElementsByTagName('disk')
for diskType in diskTypes:
    print('disk: type='+diskType.getAttribute('type')+' device='+ \
          diskType.getAttribute('device'))
    diskNodes = diskType.childNodes
    for diskNode in diskNodes:
        if diskNode.nodeName[0:1] != '#':
            print('  '+diskNode.nodeName)
            for attr in diskNode.attributes.keys():
                print('    '+diskNode.attributes[attr].name+' = '+
                 diskNode.attributes[attr].value)

conn.close()
exit(0)
