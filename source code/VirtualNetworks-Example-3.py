# Example-1.py
from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)

# lookup the default network by name
network = conn.networkLookupByName('default')
print('Virtual network default:')
print('  name: '+network.name())
print('  UUID: '+network.UUIDString())
print('  bridge: '+network.bridgeName())
print('  autostart: '+str(network.autostart()))
print('  is active: '+str(network.isActive()))
print('  is persistent: '+str(network.isPersistent()))
print()

print('Unsetting autostart')
network.setAutostart(0)
print('  autostart: '+str(network.autostart()))
print('Setting autostart')
network.setAutostart(1)
print('  autostart: '+str(network.autostart()))
print()

xml = network.XMLDesc(0)
print('XML description:')
print(xml)

conn.close()
exit(0)
