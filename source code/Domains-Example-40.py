# Example-40.py
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
devicesTypes = xml.getElementsByTagName('input')
for inputType in devicesTypes:
    print('input: type='+inputType.getAttribute('type')+' bus='+ \
          inputType.getAttribute('bus'))
    inputNodes = inputType.childNodes
    for inputNode in inputNodes:
        if inputNode.nodeName[0:1] != '#':
            print('  '+inputNode.nodeName)
            for attr in inputNode.attributes.keys():
                print('    '+inputNode.attributes[attr].name+' = '+
                 inputNode.attributes[attr].value)

conn.close()
exit(0)
