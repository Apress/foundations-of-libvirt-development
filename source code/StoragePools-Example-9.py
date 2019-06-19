# Example-9.py
from __future__ import print_function
import sys
import libvirt

stgvol_xml = """
<volume>
  <name>sparse.img</name>
  <allocation>0</allocation>
  <capacity unit="G">2</capacity>
  <target>
    <path>/var/lib/virt/images/sparse.img</path>
    <permissions>
      <owner>107</owner>
      <group>107</group>
      <mode>0744</mode>
      <label>virt_image_t</label>
    </permissions>
  </target>
</volume>"""
pool = 'default'

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)

pool = conn.storagePoolLookupByName(pool)
if pool == None:
    print('Failed to locate any StoragePool objects.', \
          file=sys.stderr)
    exit(1)

stgvol = pool.createXML(stgvol_xml, 0)
if stgvol == None:
    print('Failed to create a  StorageVol objects.', file=sys.stderr)
    exit(1)

# remove the storage volume
# physically remove the storage volume from the underlying disk media
stgvol.wipe(0)
# logically remove the storage volume from the storage pool
stgvol.delete(0)

conn.close()
exit(0)
