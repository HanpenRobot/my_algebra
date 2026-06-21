#include <stdio.h>
int load;
int min(int a[], int n)
{
    int i, min = a[0];
    for (i = 1; i < n; i++)
    {
        if (a[i] < min)
        {
            min = a[i];
        }
    }
    return min;
}

void addload(int a[], int n, int min)
{
    int i;
    for (i = 0; i < n; i++)
    {
        if (a[i] == min)
            a[i] = a[i] + load;
    }
}

int main()
{
    int i, j, containerNum;
    int weight[1000];
    int sum = 0;
    int loaded[1000];
    int p = 0;
    scanf("%d", &containerNum);
    scanf("%d", &load);
    for (j = 0; j < containerNum; j++)
    {
        scanf("%d", &weight[j]);
    }
    while (sum < load)
    {
        loaded[p] = min(weight, containerNum);
        sum = sum + min(weight, containerNum);
        addload(weight, containerNum, loaded[p]);
        p++;
    }
    for (i = 0; i < p - 1; i++)
    {
        printf("%d ", loaded[i]);
    }
    printf("\n");
    return 0;
}