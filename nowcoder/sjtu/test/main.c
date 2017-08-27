#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*

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
