from cryptography.fernet import Fernet
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("shellcode", help="shellcode to encrypt in \\xff format")
args = parser.parse_args()

# echo -n "SLAE3232SLAE3232SLAE3232SLAE3232" | base64
key = b"U0xBRTMyMzJTTEFFMzIzMlNMQUUzMjMyU0xBRTMyMzI="
f = Fernet(key)

# convert from \xaf --> af
shellcodestr = ""
i = 0
for char in args.shellcode:
    if (char == '\\'):
        continue
    elif (char == 'x'):
        continue
    else:
        shellcodestr += char

shellcodebytes = bytes.fromhex(shellcodestr)
encrypted = f.encrypt(shellcodebytes)

print('')
print("shellcodebytes: ")
print(shellcodestr + '\n')
print("encrypted: ")
print(encrypted.hex() + '\n')


