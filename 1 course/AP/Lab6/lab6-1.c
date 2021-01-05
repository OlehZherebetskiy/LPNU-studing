#include <stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
#define Size_of_text 254


int main( void )
{
   char text[Size_of_text],text1[Size_of_text];
   int Size_of_input_text, Size_of_word=0;
   
   system("clear");
   printf("Input your text(<=255 symbols):\n");
   fgets(text,255,stdin);
   
   Size_of_input_text = strlen(text);
for ( int i = 0; i <= 255; i++ )
    {
        if ( text[i] == '\n' )
        {
            text[i] = '\0';
            break;
        }
    }
int i=0;   

while (text[i]!='\0')
 {
    Size_of_word++ ;
    if (isalpha(text[i])) ;
    else
    {
        Size_of_word--;
        for (int j=1; j<=Size_of_word;j++)
        {
           text1[i-Size_of_word+j-1]=text[i-j];
        }
        Size_of_word=0; 
       text1[i]=text[i];
    }
    i++;
 }
 text1[i]='\0';

   
   printf("New text:\n\n%s\n",text1);
}
