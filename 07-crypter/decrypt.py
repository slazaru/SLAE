from cryptography.fernet import Fernet
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("shellcode", help="encrypted shellcode in afaf1f format")
args = parser.parse_args()

# echo -n "SLAE3232SLAE3232SLAE3232SLAE3232" | base64
key = b"U0xBRTMyMzJTTEFFMzIzMlNMQUUzMjMyU0xBRTMyMzI="
f = Fernet(key)

encrypted = bytes.fromhex(args.shellcode)
decrypted = f.decrypt(encrypted)

#print('')
#print("encrypted: ")
#print(encrypted.hex() + '\n')
#print("decrypted: ")
#print(f.decrypt(encrypted).hex())

shellcodestr = ""
i = 0
for char in f.decrypt(encrypted).hex():
    if (i % 2 == 0):
        shellcodestr += '\\x'
    shellcodestr += char
    i += 1
#print(shellcodestr)

cfile = open('SLAE.c', 'w')

cfile.write("unsigned char shellcode[] = \"" + shellcodestr + "\"; \n")
cfile.write("int main() { int (*ret)() = (int(*)())shellcode; ret(); }")
cfile.close()
os.system("gcc SLAE.c -fno-stack-protector -z execstack")
os.system("./a.out")

