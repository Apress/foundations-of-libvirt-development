# Example-25.py
from __future__ import print_function
import sys
import libvirt

class report_libvirt_error(libvirt.libvirtError):
    """Subclass virError to get the last error information."""
    def __init__(self, defmsg, conn=None, dom=None, net=None, \
                 pool=None, vol=None):
        libvirt.libvirtError.__init__(self, defmsg, conn=None, \
                                      dom=None, net=None, pool=None, \
                                      vol=None)
        print('Default msg:   '+str(defmsg), file=sys.stderr)
        print('Error code:    '+str(self.get_error_code()), file=sys.stderr)
        print('Error domain:  '+str(self.get_error_domain()), file=sys.stderr)
        print('Error message: '+self.get_error_message(), file=sys.stderr)
        print('Error level:   '+str(self.get_error_level()), file=sys.stderr)
        if self.err[4] != None:
            print('Error string1: '+self.get_str1(), file=sys.stderr)
        else:
            print('Error string1:', file=sys.stderr)
        if self.err[5] != None:
            print('Error string2: '+self.get_str2(), file=sys.stderr)
        else:
            print('Error string2:', file=sys.stderr)
        if self.err[6] != None:
            print('Error string3: '+self.get_str3(), file=sys.stderr)
        else:
            print('Error string3:', file=sys.stderr)
        print('Error int1:    '+str(self.get_int1()), file=sys.stderr)
        print('Error int2:    '+str(self.get_int2()), file=sys.stderr)
        exit(1)

try:
    conn = libvirt.open('qemu:///system') # invalidate the parameter 
                                          # to force an error
except libvirt.libvirtError:
    raise report_libvirt_error('Connection error')
conn.close()
exit(0)
