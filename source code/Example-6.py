# Example-6.py

import csv
import Example_5

def get_domains(filename):
    guest_domains = list()
    with open(filename) as csvfile:
        fieldnames = ['domain_name', 'ipaddress', 'userid', 'cmd']
        reader = csv.DictReader(csvfile, fieldnames)
        for row in reader:
            domain_name = row['domain_name']
            ipaddress = row['ipaddress']
            userid = row['userid']
            cmd = row['cmd']
            gd = Example_5.guest_domain(domain_name, ipaddress, \
                                        userid, cmd)
            guest_domains.append(gd)
    return guest_domains
