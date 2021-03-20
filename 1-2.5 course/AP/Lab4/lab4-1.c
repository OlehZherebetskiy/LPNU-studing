#include <stdio.h>
#include <stdlib.h>
int main(void)

{ system("clear");
    int N=100,max=-100, min=100, ser=0,i=0;
    int a[N],b[N];
    
     for ( int j = 0 ; j < 10 ; j++)
    {
        a[j]= -100 + rand() % 200;
        printf("Random number #%i:\n%i\n",j,a[j]);
    }
    
    for ( int j = 0 ; j < 10 ; j++)
    {
        if (a[j] > max) max=a[j];
        if (a[j] < min) min=a[j];
        ser+=a[j];
    }
    ser=ser/10;
     printf("Min number :%i  , Max number:%i, Average: %i\n",min,max,ser);
    for ( int j = 0 ; j < 10 ; j++)
        if (a[j] <= ser*1.1)
        {
            b[i]=a[j];
            i++;
        } ;
    
    i-=1;
            
    for ( int j = 0 ; j <= i ; j++)
    {
           printf("New number #%i:\n%i\n",j,b[j]);
    } ;
    
    
    return 0;

}
