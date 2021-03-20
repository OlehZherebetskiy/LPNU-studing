#include <stdio.h>

int main(void)
{
    int n, m, m1, n1;
    /* Inputing*/
    printf("Give me two numbers\n");
    scanf("%i %i",&n, &m);
    /* First task*/
    printf("Answers:\n");
    n1=n;m1=m;
    printf("%i\n",--m1-++n1 );
    /* Second task*/
    n1=n; m1=m;
    printf("%s\n", (m1*n)<n1++?"True":"False");
    /* Third task*/
    n1=n; m1=m;
    printf("%s\n", n1-->m1++?"True":"False");
    
    return 0;
}
