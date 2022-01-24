#include <stdio.h>
int main()
{
    int a[1000], v, n, j;
    scanf("%d", &n);
    for (v = 0; v < n; v++)
    {
        scanf("%d", &a[v]);
    }
    for (j = n - 1; j >= 0; j--)
    {
        printf("%d ", a[j]);
    }
}
