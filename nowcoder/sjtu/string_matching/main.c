#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
Syntax

The syntax for the strstr function in the C Language is:

char *strstr(const char *s1, const char *s2);
Parameters or Arguments

s1
A string to search within.
s2
The substring that you want to find.
Returns

The strstr function returns a pointer to the first occurrence s2 within the string pointed to by s1. If s2 isn't found, it returns a null pointer.

Required Header

In the C Language, the required header for the strstr function is:

#include <string.h>
*/

int main()
{
    char first[1000003];
    char second[1000003];
    int count;
    while(scanf("%s%s", first, second)!=EOF) {
        count = 0;
        char *s = first;
        while ((s = strstr(s, second))) {
            s++;
            count++;
        }
        printf("%d", count);
    }

    return 0;
}
