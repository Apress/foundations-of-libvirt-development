# Example-24.py
from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)

pages = [2048]
start = 0
cellcount = 4
buf = conn.getFreePages(pages, start, cellcount)

i = 0
for page in buf:
    print("Page Size: " + str(pages[i]) + \
          " Available pages: " + str(page))
    ++i

conn.close()
exit(0)
