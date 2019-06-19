# Example-20.py
from __future__ import print_function
import sys
import libvirt

filename = '/var/lib/libvirt/save/demo-guest.img'

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)

dom = conn.lookupByName('demo-guest')
if dom == None:
    print('Cannot find guest to be saved.', file=sys.stderr)
    exit(1)

info = dom.info()
if info == None:
    print('Cannot check guest state', file=sys.stderr)
    exit(1)

if info.state == VIR_DOMAIN_SHUTOFF:
    print('Not saving guest that is not running', file=sys.stderr)
    exit(1)

if dom.save(filename) < 0:
    print('Unable to save guest to '+filename, file=sys.stderr)

print('Guest state saved to '+filename, file=sys.stderr)

conn.close()
exit(0)
