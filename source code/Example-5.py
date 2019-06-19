# Example-5.py

class guest_domain ():
    """This class stores information about a single libvirt 
    guest domain."""
    objectname = 'guest_domain'
    domain_name = ''
    ipaddress = ''
    userid = ''
    cmd = ''
    def __init__ (self, domain_name, ipaddress, userid, cmd):
        self.domain_name = domain_name
        self.ipaddress = ipaddress
        self.userid = userid
        self.cmd = cmd
        return
