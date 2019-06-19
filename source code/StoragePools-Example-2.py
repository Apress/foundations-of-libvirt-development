# Example-2.py
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

info = pool.info()

print('Pool: '+pool.name())
print('  UUID: '+pool.UUIDString())
print('  Autostart: '+str(pool.autostart()))
print('  Is active: '+str(pool.isActive()))
print('  Is persistent: '+str(pool.isPersistent()))
print('  Num volumes: '+str(pool.numOfVolumes()))
print('  Pool state: '+str(info[0]))
print('  Capacity: '+str(info[1]))
print('  Allocation: '+str(info[2]))
print('  Available: '+str(info[3]))

conn.close()
exit(0)
