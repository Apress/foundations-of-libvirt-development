# Example-22.py
from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', \
          file=sys.stderr)
    exit(1)

xml = '<cpu mode="custom" match="exact">' + \
        '<model fallback="forbid">kvm64</model>' + \
      '</cpu>'

retc = conn.compareCPU(xml)

if retc == libvirt.VIR_CPU_COMPARE_ERROR:
    print("CPUs are not the same or ther was error.")
elif retc == libvirt.VIR_CPU_COMPARE_INCOMPATIBLE:
    print("CPUs are incompatible.")
elif retc == libvirt.VIR_CPU_COMPARE_IDENTICAL:
    print("CPUs are identical.")
elif retc == libvirt.VIR_CPU_COMPARE_SUPERSET:
    print("The host CPU is better than the one specified.")
else:
    print("An Unknown return code was emitted.")

conn.close()
exit(0)
