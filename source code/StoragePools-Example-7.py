# Example-7.py
from __future__ import print_function
import sys
import libvirt
from xml.dom import minidom

poolName = 'default'

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)

sp = conn.storagePoolLookupByName(poolName)
if sp == None:
    print('Failed to find storage pool '+poolName, \
          file=sys.stderr)
    exit(1)

stgvols = sp.listVolumes()
print('Storage pool: '+poolName)
for stgvol in stgvols :
    print('  Storage vol: '+stgvol)

conn.close()
exit(0)
