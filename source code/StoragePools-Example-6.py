# Example-6.py
from __future__ import print_function
import sys
import libvirt

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

print('Current autostart seting: '+str(sp.autostart()))
if sp.autostart() == True:
    sp.setAutostart(0)
else:
    sp.setAutostart(1)
print('Current autostart seting: '+str(sp.autostart()))

conn.close()
exit(0)
