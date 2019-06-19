#!/usr/bin/python -u

from __future__ import print_function
import argparse
import os
import time
import libvirt

# setup
"""A function for running an SSH command on an active 
   or inactive domain.
"""
__version__ = '1.0'
debug = False
uri = 'qemu:///system'
startupWait = 60  # in seconds

def toIPAddrType(addrType):
    if addrType == libvirt.VIR_IP_ADDR_TYPE_IPV4:
        return "ipv4"
    elif addrType == libvirt.VIR_IP_ADDR_TYPE_IPV6:
        return "ipv6"

def runJob(domain_name, userid, cmd, restoreFile='', open_connx=None):
    # get the connection
    if open_connx == None:
        connx = libvirt.open(uri)
    else:
        connx = open_connx
    # get the domain
    domain = connx.lookupByName(domain_name)
    if domain == None:
        if open_connx == None:
            connx.close()
        return
    # start/restore the domain if necessary
    wasActive = domain.isActive()
    if debug == True:
        print('wasActive = '+str(wasActive))
    if restoreFile != '' and wasActive == False:
        if debug == True:
            print('Restoring domain')
        domain.restore(restoreFile)
    elif restoreFile != '' and wasActive == True:
        if debug == True:
            print('Domain was active')
        pass
    elif wasActive == False:
        if debug == True:
            print('Starting domain -- sleeping')
        if domain.create() < 0:
            print('Error: Domain is not active or never started.')
            return(-1)
        time.sleep(startupWait)
    else:
        if debug == True:
            print('Domain was active')
        pass
    # make sure the domain is running
    if domain.isActive() == False:
        print('Error: Domain is not active or never started.')
        return(-1)
    # get the ip address of the domain
    ifaces = domain.interfaceAddresses( \
             libvirt.VIR_DOMAIN_INTERFACE_ADDRESSES_SRC_AGENT, 0)
    usableIpaddr = None
    for (name, val) in ifaces.iteritems():
        if val['addrs']:
            for ipaddr in val['addrs']:
                if debug == True:
                    print(str(ipaddr))
                if ipaddr['addr'][0:8] == '192.168.' and \
                 toIPAddrType(ipaddr['type']) == 'ipv4':
                    usableIpaddr = ipaddr['addr']
                    break
                if ipaddr['addr'][0:3] == '10.' and \
                    toIPAddrType(ipaddr['type']) == 'ipv4':
                    usableIpaddr = ipaddr['addr']
                    break
                # currently we ignore ipv6 addresses
    # run the SSH command
    if usableIpaddr == None:
        print('Error: No usable ipaddress was found.')
        return(-1)
    sshcmd = 'ssh %s@%s %s' % (userid, usableIpaddr, cmd)
    os.system(sshcmd)
    # shutdown the domain if necessary
    if wasActive == False:
        if restoreFile != '':
            domain.save(restoreFile)
        else:
            domain.shutdown()
    # close the connection if necessary
    if open_connx == None:
        connx.close()
    return(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser( \
        description='Proess runJobOnDomain command line arguments.', \
        version=__version__)
    parser.add_argument('--domain', \
                        help='the domain to be used to run the job.')
    parser.add_argument('--userid', \
                        help='the SSH userid for the job.')
    parser.add_argument('--cmd', \
                      help='the SSH command to be run on the domain.')
    args = parser.parse_args()
    # get the arguments
    domain = args.domain
    userid = args.userid
    cmd = args.cmd
    if debug == True:
        print('The command line arguments were:')
        print('domain = '+domain)
        print('userid = '+userid)
        print('cmd = '+cmd)
    retc = runJob(domain, userid, cmd, '')
    exit(0)
