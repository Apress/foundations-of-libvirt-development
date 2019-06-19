# Example-26.py
from __future__ import print_function
import sys
import libvirt

def libvirt_error_handler(ctx, err):
    print('Error code:    '+str(err[0]), file=sys.stderr)
    print('Error domain:  '+str(err[1]), file=sys.stderr)
    print('Error message: '+err[2], file=sys.stderr)
    print('Error level:   '+str(err[3]), file=sys.stderr)
    if err[4] != None:
        print('Error string1: '+err[4], file=sys.stderr)
    else:
        print('Error string1:', file=sys.stderr)
    if err[5] != None:
        print('Error string2: '+err[5], file=sys.stderr)
    else:
        print('Error string2:', file=sys.stderr)
    if err[6] != None:
        print('Error string3: '+err[6], file=sys.stderr)
    else:
        print('Error string3:', file=sys.stderr)
    print('Error int1:    '+str(err[7]), file=sys.stderr)
    print('Error int2:    '+str(err[8]), file=sys.stderr)
    exit(1)

ctx = 'just some information'
libvirt.registerErrorHandler(libvirt_error_handler, ctx)

conn = libvirt.open('qemu:///system') # invalidate the parameter 
                                      # to force an error

conn.close()
exit(0)
