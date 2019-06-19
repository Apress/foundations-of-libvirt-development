# Example-14.py
from __future__ import print_function
import sys
import libvirt

xmlconfig = '<domain>........</domain>'

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)

dom = conn.createXML(xmlconfig, 0)
if dom == None:
    print('Unable to boot transient guest configuration.', \
          file=sys.stderr)
    exit(1)

print('Guest '+dom.name()+' has booted', file=sys.stderr)

conn.close()
exit(0)
