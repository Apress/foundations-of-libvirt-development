# Example-56.py
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

state, reason = dom.state()

if state == libvirt.VIR_DOMAIN_NOSTATE:
    print('The state is VIR_DOMAIN_NOSTATE')
elif state == libvirt.VIR_DOMAIN_RUNNING:
    print('The state is VIR_DOMAIN_RUNNING')
elif state == libvirt.VIR_DOMAIN_BLOCKED:
    print('The state is VIR_DOMAIN_BLOCKED')
elif state == libvirt.VIR_DOMAIN_PAUSED:
    print('The state is VIR_DOMAIN_PAUSED')
elif state == libvirt.VIR_DOMAIN_SHUTDOWN:
    print('The state is VIR_DOMAIN_SHUTDOWN')
elif state == libvirt.VIR_DOMAIN_SHUTOFF:
    print('The state is VIR_DOMAIN_SHUTOFF')
elif state == libvirt.VIR_DOMAIN_CRASHED:
    print('The state is VIR_DOMAIN_CRASHED')
elif state == libvirt.VIR_DOMAIN_PMSUSPENDED:
    print('The state is VIR_DOMAIN_PMSUSPENDED')
else:
    print(' The state is unknown.')
print('The reason code is ' + str(reason))

conn.close()
exit(0)
