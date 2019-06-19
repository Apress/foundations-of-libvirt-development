#!/usr/bin/python
# Example ??
# by W. David Ashley


from __future__ import print_function
import sys
import libvirt_qemu as qemu
import libvirt
import json
from xml.dom import minidom


# global variables
domainName = 'rhel71-x86_64-1'

# get a connection to the system
connx = libvirt.open('qemu:///system')
if connx == None:
    print('Failed to open connection to qemu:///system.', file=sys.stderr)
    exit(1)

# get the domain object
domain = connx.lookupByName(domainName)
if domain == None:
    print('Failed to get domain object.', file=sys.stderr)
    exit(1)

# get the mac address of the first network interface (network or bridge)
macAddress = ''
rawXml = domain.XMLDesc(0)
xml = minidom.parseString(rawXml)
interfaceTypes = xml.getElementsByTagName('interface')
for interfaceType in interfaceTypes:
    # note that we only look for the first network or bridge interface,
    # if other other search critera are needed it should be implemented here
    if interfaceType.getAttribute('type') == 'bridge' or \
     interfaceType.getAttribute('type') == 'network':
        interfaceNodes = interfaceType.childNodes
        for interfaceNode in interfaceNodes:
            if interfaceNode.nodeName == 'mac':
                for attr in interfaceNode.attributes.keys():
                    if interfaceNode.attributes[attr].name == 'address':
                        macAddress = interfaceNode.attributes[attr].value
                        break
if macAddress == '':
    print('Failed to get mac address.', file=sys.stderr)
    exit(1)

# query the qemu-guest-agent for the network interfaces
cmd = '{"execute":"guest-network-get-interfaces"}'
timeout = qemu.VIR_DOMAIN_QEMU_AGENT_COMMAND_BLOCK
flags = 0
result = qemu.qemuAgentCommand(domain, cmd, timeout, flags)
if result == None:
    print('Failed to communicate with the qemu-guest-agent.', file=sys.stderr)
    exit(1)

# print out the ipv4 address that matches the previously obtained mac address
decoded = json.loads(result)
for hwaddr in decoded['return']:
    if hwaddr['hardware-address'] == macAddress:
        print(macAddress)
        for ipaddr in hwaddr['ip-addresses']:
            if ipaddr['ip-address-type'] == 'ipv4':
                print('    '+ipaddr['ip-address'])

