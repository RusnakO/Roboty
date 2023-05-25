S = input ()
en_Up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SN = ''
for C in S:
    if C in en_Up:
        C = C.lower()
    SN=SN+C
print (SN)
