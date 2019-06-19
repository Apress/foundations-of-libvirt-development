# Example-40.py
from __future__ import print_function
import sys
import libvirt


domxml =
 """<domain type='kvm'>
      <name>example</name>
      <memory>131072</memory>
      <vcpu>1</vcpu>
      <os>
        <type arch='x86_64' machine='pc-0.13'>hvm</type>
      </os>
      <devices>
        <disk type='file' device='disk'>
          <driver name='qemu' type='qed'/>
          <source file='/var/lib/libvirt/images/example.qed' />
          <target dev='vda' bus='virtio'/>
        </disk>
      </devices>
    </domain>"""

def do_cmd (cmdline):
    status = os.system(cmdline)
    if status < 0:
        return -1
    return WEXITSTATUS(status)

def make_domain (conn)
    do_cmd("qemu-img create -f raw " + \
           "/var/lib/libvirt/images/backing.qed 100M")
    do_cmd("qemu-img create -f qed -b " + \
           "/var/lib/libvirt/images/backing.qed"+ \
           "/var/lib/libvirt/images/example.qed")
    dom = conn.createXML(domxml, 0)
    return dom


virConnectPtr conn
dom = None
disk = "/var/lib/libvirt/images/example.qed"

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)

dom = make_domain(conn)
if dom == None:
    print("Failed to create domain", file=sys.stderr)
    exit(1)

if dom.blockPull(disk, 0, 0) < 0:
    print("Failed to start block pull", file=sys.stderr)
    exit(1)

while (1):
    info = dom.blockJobInfo(disk, 0);
    if (info != None:
        print("BlockPull progress: %0.0f %%",
            float(100 * info.cur / info.end))
    elif info.cur == info.end):
        printf("BlockPull complete")
        break
    else:
        print("Failed to query block jobs", file=os.stderr)
        break
    time.sleep(1)

os.unlink("/var/lib/libvirt/images/backing.qed")
os.unlink("/var/lib/libvirt/images/example.qed")
if dom != NULL:
   conn.destroy(dom)

conn.close()
exit(0)
