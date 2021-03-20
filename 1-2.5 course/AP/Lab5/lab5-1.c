#include <stdio.h>
#include <stdlib.h>
#define Size_mas_std 100
#define random_min -10
#define random_max 10

// Operation
int Max(int size_i,int size_j,int a[Size_mas_std][Size_mas_std])
    {
        int max=random_min;
            for(int j=0; j < size_j; j++)
            {
                if (max<a[size_i][j]) max=a[size_i][j];
            
            }
        return max;
    }
//"printf" function for array   
void print_ar (int size_mas_i,int size_mas_j,int a[Size_mas_std][Size_mas_std])
{
 for (int i=0;i < size_mas_i; i++)
        {
            for(int j=0; j < size_mas_j; j++)
            {
                if (a[i][j]>=0) printf(" ");
                if (a[i][j]<10 && a[i][j]>-10 ) printf(" ");
                if (a[i][j]==0) 
                { 
                   printf("  ");
                }
                else
                    printf("%i ",a[i][j]);
            }
            
            printf("\n");
        }
}

//main part
int main(void)
{
    int size_mas_i,size_mas_j,input_style;
    int a[Size_mas_std][Size_mas_std],help[Size_mas_std][Size_mas_std];
    
    system("clear");
//input size of array    
    printf("Number of rows : ");
   do  scanf("%i",&size_mas_i); while (size_mas_i<1);
    printf("Number of columns (better if it will be <11) : ");
   do scanf("%i",&size_mas_j); while (size_mas_i<1);
    
    system("clear");
//input the type of filling    
    printf("How do you want to fill your array\n using random -- press 1\ninput all numbers -- press 2\n");
    do scanf("%i",&input_style); while (input_style >2 || input_style <1);
    
    system("clear");
//two styles of filling    
    if (input_style==1) 
    {
        for (int i=0;i < size_mas_i; i++)
        {
            for(int j=0; j < size_mas_j; j++)
            a[i][j]= random_min + rand() % (random_max-random_min);
        } 
    }
    else 
        for (int i=0;i < size_mas_i; i++)
        {
            for(int j=0; j < size_mas_j; j++)
            {
                printf("Input [%i][%i] number in array: ",i,j);
                scanf("%i",&a[i][j]);
            }
        } 
        
   
 //output of array  
   printf("Here is your array:\n");
   print_ar(size_mas_i,size_mas_j,a);
   
 //work on an array  
    for (int i=0,max_l;i < size_mas_i; i++)
        {
            max_l=Max(i,size_mas_j,a);
            for(int j=0; j < size_mas_j; j++)
            {
                help[i][j+max_l]=a[i][j];
            }
        }
    
 //output of final array   
    printf("New array after operation:\n");
    print_ar(size_mas_i,size_mas_j+random_max,help);
}
