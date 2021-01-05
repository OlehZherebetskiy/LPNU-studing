#include <stdio.h>
#include <math.h>

int main (void)
{
    float a1, b1;
    double a2, b2;
    
    printf("Give me two numbers for floats\n");
    scanf("%f %f",&a1, &b1);
    printf("Float out :%f\n",(pow(a1+b1,2) - (pow(a1, 2)+ 2*a1*b1))/pow(b1,2));
    
    printf("Give me two numbers for double\n");
    scanf("%lf %lf",&a2, &b2);
    printf("Double out :%lf\n",(pow(a2+b2,2) - (pow(a2, 2)+ 2*a2*b2))/pow(b2,2));
    
    return 0;
}
    
