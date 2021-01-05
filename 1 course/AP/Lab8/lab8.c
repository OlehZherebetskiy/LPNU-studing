 #include<stdio.h>
#include<stdlib.h>

typedef struct
{
char name [40];
char author [40];
float duration;
float cost;
}mdisk;



int inp_struk(void)
{
  int num;
  printf("Input number of disks:");
  scanf("%d",&num);
  mdisk ptr ;
  FILE *fl=fopen("f.dat", "wb+");
  for(int i=0; i<num;i++)
  {
   printf("Name :");scanf("%s",ptr.name);
   printf("Author : ");scanf("%s",ptr.author);
   printf("Duration: ");scanf("%f",&ptr.duration);
   printf("Cost: ");scanf("%f",&ptr.cost);
   fwrite(&ptr, sizeof(mdisk),1,fl);

   if (ferror(fl)!=0) exit(1);
  }


  fclose(fl);
  return num;
}



void del_by_dur(int dur,int num)
{
 mdisk mas[num];
  FILE *fl=fopen("f.dat", "rb");
  int i=0;
  while(!feof(fl)&&i<=num)
 {
  fread(&mas[i], sizeof(mdisk),1,fl);
  i++;
 }
  fclose(fl);
  fl=fopen("fl.dat", "wb");
 for (i=0; i<num;i++)
 {
  if (mas[i].duration!=dur)
  {
    fwrite(&mas[i], sizeof(mdisk),1,fl);
  }
 }
 fclose(fl);

}

void add_by_num(int nadd)
{
mdisk mas[100];
  FILE *fl=fopen("f.dat", "rb");
  int i=0;
  while(!feof(fl))
 {
  fread(&mas[i], sizeof(mdisk),1,fl);
  i++;
 }
 int num=i-1;
  fclose(fl);
  fl=fopen("fil.dat", "wb");
 for (i=0; i<num;i++)
 {
  fwrite(&mas[i], sizeof(mdisk),1,fl);
  if (i+1==nadd)
  {
    mdisk ptr;
    for(int j=0;j<2;j++)
    {
     printf("Name :");scanf("%s",ptr.name);
     printf("Author : ");scanf("%s",ptr.author);
     printf("Duration: ");scanf("%f",&ptr.duration);
     printf("Cost: ");scanf("%f",&ptr.cost);
     fwrite(&ptr, sizeof(mdisk),1,fl);
    }
  }
 }
 fclose(fl);
}

void print_disk(char *file)
{
  mdisk mas[100];
  FILE *fl=fopen(file, "r");
  int i=0;
  while(!feof(fl))
 {
  fread(&mas[i], sizeof(mdisk),1,fl);
  i++;
 }
 int num=i-1;
  fclose(fl);
  for(i=0;i<num;i++)
  {
     printf("Name : %s  ",mas[i].name);
     printf("Author : %s  ",mas[i].author);
     printf("Duration: %f  ",mas[i].duration);
     printf("Cost: %f  \n",mas[i].cost);

  }
}


int main (void)
{



int number_st=inp_struk();
char * k = "f.dat";
print_disk(k);

int dur;
int num_add;
printf("Input duration of disk you want to delete:"); scanf("%d",&dur);

del_by_dur(dur,number_st);
 k = "fl.dat";
print_disk(k);

printf("Input number of disk after which you want to add two disks:"); scanf("%d",&num_add);


add_by_num(num_add);
 k = "fil.dat";
print_disk(k);


}
