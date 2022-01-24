#include<stdio.h>
int main()
{
  int sum=0,k,i,j,l,max=-30;
  int arr[6][6]; 
  for(i=0;i<6;i++) 
  {
    for(j=0;j<6;j++)
    {
      scanf("%d",&arr[i][j]);
    }
  }
  for(l=0;l<4;l++)
  
  
  {
    for(i=0;i<4;i++)
    {
      sum=0;
      for(j=i;j<i+3;j++)
      {
       
        if(j==i+1)
        {
          sum=sum+arr[i+1][l+1];
        }
        else
        {
          for(k=0;k<3;k++)
          {
            sum=sum+arr[j][l+k];
          }
        }
      }
      if(sum>max)
      {
        max=sum;

      }
    }
  }
  printf("%d",max);
}
