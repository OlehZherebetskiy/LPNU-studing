#include <stdio.h>
#include <math.h>

int main (void)
{
    double a=0.1,b=0.8,s=0.0,s1=0.0,y , x=b;
    int n=35,j=1;
    for (; x>=a-0.03; x-=((b-a)/10))
    {
     printf( "X= %lf   ",x);
     
    for (int i=1; i<=n; i++)
        s+=pow(x,i)*cos(i*3.14/3.0)/i;
    printf( "SN= %lf   ",s);
    
   do { y=pow(x,j)*cos(j*3.14/3.0)/j;
        s1+=y;j++;}
   while (y>0.0001 || y<-0.0001);
    printf( "SE= %lf   ",s1);
    
    printf( "Y= %f  \n",(-1)*log(1-2*x*cos (3.14/3)+pow(x,2))/2);
    s=0;s1=0;j=1;
    
      
    }
}
