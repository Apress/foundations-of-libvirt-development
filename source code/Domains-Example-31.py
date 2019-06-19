# Example-31.py
from __future__ import print_function
import sys
import libvirt

domName = 'Fedora22-x86_64-1'

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)

dom = conn.lookupByID(6)
if dom == None:
    print('Failed to find the domain '+domName, file=sys.stderr)
    exit(1)

rd_req, rd_bytes, wr_req, wr_bytes, err = \
dom.blockStats('/path/to/linux-0.2.img')
print('Read requests issued:  '+str(rd_req))
print('Bytes read:            '+str(rd_bytes))
print('Write requests issued: '+str(wr_req))
print('Bytes written:         '+str(wr_bytes))
print('Number of errors:      '+str(err))

conn.close()
exit(0)
