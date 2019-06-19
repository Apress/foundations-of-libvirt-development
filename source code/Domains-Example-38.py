# Example-38.py
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
interfaceTypes = xml.getElementsByTagName('interface')
for interfaceType in interfaceTypes:
    print('interface: type='+interfaceType.getAttribute('type'))
    interfaceNodes = interfaceType.childNodes
    for interfaceNode in interfaceNodes:
        if interfaceNode.nodeName[0:1] != '#':
            print('  '+interfaceNode.nodeName)
            for attr in interfaceNode.attributes.keys():
                print('    '+interfaceNode.attributes[attr].name+' = '+
                 interfaceNode.attributes[attr].value)

conn.close()
exit(0)
