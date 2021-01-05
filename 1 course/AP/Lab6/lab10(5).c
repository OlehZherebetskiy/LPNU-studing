#include <stdio.h>
#include <stdlib.h>
#define Max 100;
#define Min -100;

typedef struct Num{
    int number;
    struct Num *next;

}Num;

Num *head=NULL;
Num *head1=NULL;


int main (void)

{ system("clear");
       int ser=0,max=0,min=Max;



     for ( int j = 0 ; j < 10 ; j++)
    {
        Num *a = (Num*)malloc(sizeof(Num));
        a->next = head1;
        head1 = a;
        a->number=  rand() % Max;
        printf("Random number %i\n",a->number);
    }
    Num * a = head1;


     while(a != NULL)
    {
        if (a->number > max) max=a->number;
        if (a->number < min) min=a->number;
        ser+=a->number;
        a = a->next;
    }
    ser=ser/10;
     printf("Min number :%i  , Max number:%i, Average: %i\n",min,max,ser);
     a=head1;
    while(a != NULL)
    {
        if (a->number <= ser*1.1)
        {
            Num *b = (Num*)malloc(sizeof(Num));
             b->next = head;
             head = b;
            b->number=a->number;

        } ;
        a = a->next;
    }

  Num * b=head;
     while(b != NULL)
     {
           printf("New number :  %i  \n", b->number);
           b=b->next;
     } ;


    return 0;

}
