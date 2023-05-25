s1 = input ()
a = list(s1)
a.reverse()
s2 = ''.join(a)
if s1 == s2:
    print ('PALINDROM')
else:
    print ('NO PALINDROM')
