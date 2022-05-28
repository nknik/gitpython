#include <stdio.h>
#include <stdlib.h>
int main()
{
    int SampleInput, result, r, i;
    int n = 0;
    int k = 0;
    printf("Enter the first number for the range: ");
    scanf("%d", &SampleInput); // received the number for num1

    result = 0;
    while (SampleInput)
    {
        k = SampleInput % 10;
        r = k % 2;
        if (r != 0)
            result += k;
        SampleInput = SampleInput / 10;
    }

    printf("%d %d", result, k);
    getch();
    return 0;
}