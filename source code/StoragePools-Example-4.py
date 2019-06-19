# Example-4.py
from __future__ import print_function
import sys
import libvirt
xmlDesc = """
<pool type='dir'>
  <name>mypool</name>
  <uuid>8c79f996-cb2a-d24d-9822-ac7547ab2d01</uuid>
  <capacity unit='bytes'>4306780815</capacity>
  <allocation unit='bytes'>237457858</allocation>
  <available unit='bytes'>4069322956</available>
  <source>
  </source>
  <target>
    <path>/home/dashley/images</path>
    <permissions>
      <mode>0755</mode>
      <owner>-1</owner>
      <group>-1</group>
    </permissions>
  </target>
</pool>"""

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)

# create a new persistent storage pool
pool = conn.storagePoolDefineXML(xmlDesc, 0)
if pool == None:
    print('Failed to create StoragePool object.', \
          file=sys.stderr)
    exit(1)

# destroy the storage pool
pool.undefine()

# create a new non-persistent storage pool
pool = conn.storagePoolCreateXML(xmlDesc, 0)
if pool == None:
    print('Failed to create StoragePool object.', \
          file=sys.stderr)
    exit(1)

# destroy the storage pool
pool.undefine()

conn.close()
exit(0)
