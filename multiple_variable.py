###################################################
# OLD WAY
###################################################
a = 10
b = 20
c = 30
d = [None]*3
d[0] = a
d[1] = b
d[2] = c
print(f'a={a}, b={b}, c={c}')
print(f'd={d}')

###################################################
# PYTHONIC WAY
###################################################
x, y, z = 10, 20, 30
p = x, y, z
# p = [x, y, z]
print(f'x={x}, y={y}, z={z}')
print(p)
