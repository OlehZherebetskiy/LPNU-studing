#include <stdio.h>
#include <math.h>


int main(void)
{
    double x=1,a = 1, eps=0.0001;
    int n=0;
     
    printf("Result %lf With n= %i With last x= %lf\n", a,n,x);
    do
    {
       
        x*= 2*pow(n,n)/pow(n+1,n);
        a+= x; 
        n++;
        printf("Result %lf With n= %i With last x= %lf\n", a,n,x);
    }while(x > eps); 
}
