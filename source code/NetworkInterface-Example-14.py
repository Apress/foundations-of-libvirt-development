# Example-14.py
from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)

domainName = 'CentOS7'
dom = conn.lookupByName(domainName)
if dom == None:
    print('Failed to get the domain object', file=sys.stderr)

ifaces = \
  dom.interfaceAddresses(libvirt.VIR_DOMAIN_INTERFACE_ADDRESSES_SRC_AGENT, \
                         0)

print("The interface IP addresses:")
for (name, val) in ifaces.iteritems():
    if val['addrs']:
        for ipaddr in val['addrs']:
            if ipaddr['type'] == libvirt.VIR_IP_ADDR_TYPE_IPV4:
                print(ipaddr['addr'] + " VIR_IP_ADDR_TYPE_IPV4")
            elif ipaddr['type'] == libvirt.VIR_IP_ADDR_TYPE_IPV6:
                print(ipaddr['addr'] + " VIR_IP_ADDR_TYPE_IPV6")

conn.close()
exit(0)
