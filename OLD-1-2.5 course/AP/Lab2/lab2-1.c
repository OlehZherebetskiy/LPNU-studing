#include <stdio.h>
#include <math.h>

int fact(int i)
{
    int j=1;
    for(;i>0;j=j*i--) ;

    return j ; 
}


int main(void)
{
    double x,a = 0.0, eps=0.0001;
    int n=0;
    
    do
    {
       
        x = (pow(2,n)*fact(n))/pow(n,n);
        a+= x; 
        printf("Result %lf With n= %i With last x= %lf\n", a,n,x);
        n++;
    }while(x > eps); 
}
