# Example-03.py
from __future__ import print_function
import sys
import libvirt, libvirt_qemu

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)

domainName = 'centos7.0'
dom = conn.lookupByName(domainName)
if dom == None:
    print('Failed to get the domain object', file=sys.stderr)

ret_json = libvirt_qemu.qemuAgentCommand(dom, '{"execute": "guest-set-time"}',
                libvirt_qemu.VIR_DOMAIN_QEMU_AGENT_COMMAND_DEFAULT, 0)
if ret_json == None:
    print('Failed to get the JSON object', file=sys.stderr)
else:
    print(ret_json)

conn.close()
