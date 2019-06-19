# Example-8.py
from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)

pool = conn.storagePoolLookupByName('default')
if pool == None:
    print('Failed to locate any StoragePool objects.', \
          file=sys.stderr)
    exit(1)

stgvols = pool.listVolumes()

print('Pool: '+pool.name())
for stgvolname in stgvols:
    print('  Volume: '+stgvolname)
    stgvol = pool.storageVolLookupByName(stgvolname)
    info = stgvol.info()
    print('    Type: '+str(info[0]))
    print('    Capacity: '+str(info[1]))
    print('    Allocation: '+str(info[2]))

conn.close()
exit(0)
