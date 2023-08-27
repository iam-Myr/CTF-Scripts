def solve(s, flag):
    end = len(s)
    for i in range (4, end):
        s[i] = s[i-4] ^ flag[i - 4]

    y = ""
    for i in s:
        y += chr(i)
    print (y)

def main():
    s = [116,106,99,116, 102,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    flag= [18, 17, 0, 21, 11, 72, 60, 18, 12, 68, 0, 16, 81, 25, 46, 22, 3, 28, 66, 17, 10, 74, 114, 86, 13, 122, 116, 79, 0 ]
    solve(s,flag)

main()
