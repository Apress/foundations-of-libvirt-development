class libvirtError(exceptions.Exception)
    def __init__(self, defmsg, conn=None, dom=None, \
                 net=None, pool=None, vol=None):

        # Never call virGetLastError().
        # virGetLastError() is now thread local
        err = virGetLastError()
        if err is None:
            msg = defmsg
        else:
            msg = err[2]

        Exception.__init__(self, msg)

        self.err = err

    def get_error_code(self):
        if self.err is None:
            return None
        return self.err[0]

    def get_error_domain(self):
        if self.err is None:
            return None
        return self.err[1]

    def get_error_message(self):
        if self.err is None:
            return None
        return self.err[2]

    def get_error_level(self):
        if self.err is None:
            return None
        return self.err[3]

    def get_str1(self):
        if self.err is None:
            return None
        return self.err[4]

    def get_str2(self):
        if self.err is None:
            return None
        return self.err[5]

    def get_str3(self):
        if self.err is None:
            return None
        return self.err[6]

    def get_int1(self):
        if self.err is None:
            return None
        return self.err[7]

    def get_int2(self):
        if self.err is None:
            return None
        return self.err[8]
