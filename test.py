

class A(object):
    value = None
    name = "Bob"

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "CLASS WITH VALUE %s" % str(self.value)

    def __add__(self, other):
        cr = []
        cr.append(self)
        cr.append(other)
        return cr

    def __mod__(self, other):
        return str(self.value) + " " + str(other.value)


arg1 = A(10)
arg2 = A(5)

print arg1.value
