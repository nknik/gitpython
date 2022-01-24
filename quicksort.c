#include<stdio.h>
#include<stdlib.h>
// #include <string.h>
// #include<convio.h>
int main(int argc, char const *argv[])
{
    /* code */
    int a[]={5,4,3,2,1};
    int i, j,nk,tmp;
    char str[100];
int n=5;

for (i = 0; i < n-1; i++){
    for (j = 0; j < n-i-1; j++){
        if (a[j] > a[j+1]){
              tmp=a[j];
              a[j]=a[j+1];
              a[j+1]=tmp;
              }
    }
}
printf("enter");
scanf("%s",str);
for ( i = 0; i < strlen(str); i++)
{

if (str[i] >= 'a' && str[i] <= 'z')
    {
        str[i]=str[i] - 32;
    }
    else if (str[i] >= 'A' && str[i] <= 'Z')
    {
       str[i]= str[i] + 32;
    }
}

for ( i = 0; i < n; i++)
{
    /* code */
    printf("%c",str[i]);
}

    return 0;
}
