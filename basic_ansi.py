from __future__ import print_function
import itertools

# basic coloring:
# 39/49: default text color
# 30/40: low intensity color
# 90/100: high intensity color

for bg in itertools.chain(range(49,50),range(40,48),range(100,108)):
    out = []
    for fg in itertools.chain(range(39,40),range(30,38),range(90,98)):
        out.append('\x1b[%i;%im%-6s\x1b[0m ' % (fg,bg,('%i;%i'%(fg,bg))))
    print(' '.join(out))
print()
print('\x1b[1mbold\x1b[0m')
print('\x1b[3mitalic\x1b[0m')
print('\x1b[4munderline\x1b[0m')
print('\x1b[5mblink\x1b[0m')
print('\x1b[9mcrossed-out\x1b[0m')
