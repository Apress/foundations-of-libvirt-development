# Example-58.py
from __future__ import print_function
import libvirt

# setup
"""List network interface IP Addresses for a guest domain.
"""

domName = 'CentOS7'

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)

domain = conn.lookupByName(domName)
if domain == None:
    print('Failed to find the domain '+domName, file=sys.stderr)
    exit(1)

# make sure the domain is running
if domain.isActive() == False:
    print('Error: Domain is not active or never started.')
    exit(1)

# get and list the ip addresses, use QEMU as the source information
ifaces = domain.interfaceAddresses(libvirt. \
                VIR_DOMAIN_INTERFACE_ADDRESSES_SRC_AGENT, 0)
for (name, val) in ifaces.iteritems():
    if val['addrs']:
        for ipaddr in val['addrs']:
            print(name+' '+str(ipaddr))

conn.close()
exit(0)
