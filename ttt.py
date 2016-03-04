import units

a = units.Unit("aaa")
b = units.Unit("bbbb")
c = units.Unit("ccccc")
d = units.Unit("aaa")

i = [a, b, c]

for ii in i:
    if d.name == ii.name:
        print "ok"