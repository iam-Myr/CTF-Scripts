match = "~{k|ns0;<cW<f|9Wl;j}oo;z{W<z;Wf8We<|k`Wn8zW|`;W;9;;?u"
dest = "s3cR3ts3x"

def XorAndRecurse(a1, a2):
    if a2 <= 3:
        return XorAndRecurse(ord(dest[3 * a2]) ^ a1, a2 + 1)  # dest[0], dest[3], dest[6], dest[9]
    else:
        return a1
def lastXor(a1):
    return a1 ^ 0x12
def encrypt(a):
    v4 = XorAndRecurse(ord(a), 0)
    return chr(lastXor(v4))

length = len(match)
for x in range(125, 32, -1):
    dest = dest + chr(x)
    flag = ""
    for i in range(length):
        for j in range(125, 23, -1):
            result = encrypt(chr(j))
            if result == match[i]:
                flag += chr(j)
                break
    if "vsctf" in flag:
        print(flag)
    dest = dest[:9]  # Cut 10th character
