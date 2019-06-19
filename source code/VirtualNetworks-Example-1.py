# Example-1.py
from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)

# discover all the virtual networks
networks = conn.listNetworks()
print('Virtual networks:')
for network in networks:
    print('  '+network)
print()

# lookup the default network by name
network = conn.networkLookupByName('default')
print('Virtual network default:')
print('  name: '+network.name())
uuid = network.UUIDString()
print('  UUID: '+uuid)
print('  bridge: '+network.bridgeName())
print()

# lookup the default network by name
network = conn.networkLookupByUUIDString(uuid)
print('Virtual network default:')
print('  name: '+network.name())
print('  UUID: '+network.UUIDString())
print('  bridge: '+network.bridgeName())

conn.close()
exit(0)
