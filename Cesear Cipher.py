## Hackerrank: Cesear Cipher

n = 90
s = '!m-rB`-oN!.W`cLAcVbN/CqSoolII!SImji.!w/`Xu`uZa1TWPRq`uRBtok`xPT`lL-zPTc.BSRIhu..-!.!tcl!-U'
k = 62

upper = 'QWERTYUIOPASDFGHJKLZXCVBNM'
lower = 'qwertyuiopasdfghjklzxcvbnm'

line = []

while k >= 26:
    k -= 26

for each in s:
    if each in upper or each in lower:
        if each in upper and chr(ord(each) + k) in upper:
            line.append(chr(ord(each) + k))
        elif each in upper and chr(ord(each) + k) in lower:
            line.append(chr(ord(each) - 26 + k))
        elif each in lower and chr(ord(each) + k) in lower:
            line.append(chr(ord(each) + k))
        elif each in lower and chr(ord(each) - 26) in upper:
            line.append(chr(ord(each) - 26 + k))
        else:
            line.append(chr(ord(each) - 26 + k))
    else:
        line.append(each)

print(''.join(line))
