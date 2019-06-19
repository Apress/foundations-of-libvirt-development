# Example-7.py

import csv
import Example_6

guest_domains = Example_6.get_domains('Example-myprojectbuild.csv')
for gd in guest_domains:
    print gd.domain_name + ',' + gd.ipaddress + ',' + gd.userid + ',' \
    + gd.cmd
