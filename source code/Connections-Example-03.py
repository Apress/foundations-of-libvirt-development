# Example-3.py
from __future__ import print_function
import sys
import libvirt

SASL_USER = "my-super-user"
SASL_PASS = "my-super-pass"

def request_cred(credentials, user_data):
    for credential in credentials:
        if credential[0] == libvirt.VIR_CRED_AUTHNAME:
            credential[4] = SASL_USER
        elif credential[0] == libvirt.VIR_CRED_PASSPHRASE:
            credential[4] = SASL_PASS
    return 0

auth = [[libvirt.VIR_CRED_AUTHNAME, libvirt.VIR_CRED_PASSPHRASE], \
        request_cred, None]

conn = libvirt.openAuth('qemu+tcp://localhost/system', auth, 0)
if conn == None:
    print('Failed to open connection to qemu+tcp://localhost/system', \
          file=sys.stderr)
    exit(1)
conn.close()
exit(0)
