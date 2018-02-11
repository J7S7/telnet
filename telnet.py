import telnetlib
import re


numberlist = []
a = ['eth1', 'askdjeth2', 'Eth3', 'sldfj', 'lskdjfEth1', '324']
pattern = re.compile(r'(.*)eth(.*)', re.I)
for i in a:
    b = pattern.match(i)
    if b is not None:
        c = b.group(0)
        numberlist.append(c)
print numberlist
