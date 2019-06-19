# Example-50.py
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

state, maxmem, mem, cpus, cput = dom.info()
print('The state is ' + str(state))
print('The max memory is ' + str(maxmem))
print('The memory is ' + str(mem))
print('The number of cpus is ' + str(cpus))
print('The cpu time is ' + str(cput))

conn.close()
exit(0)
