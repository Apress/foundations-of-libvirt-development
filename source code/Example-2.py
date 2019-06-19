# Example-2.py
from __future__ import print_function
import sys
import libvirt

# obtain a connection to the libvirt system
conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

# obtain a guest domain instance
domainName = 'someguest'
dom = conn.lookupByName(domainname)
if dom == None:
    print('Failed to get the domain object', file=sys.stderr)

# at this point you can now control aspects of the domain
# through the methods of the domain instance

# close the connection to the libvirt system
conn.close()
