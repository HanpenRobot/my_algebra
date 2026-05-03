#include <stdio.h>
#include <math.h>
#include <stdlib.h>

void henon_map()
{
    double a = 1.4, b = 0.3;
    double x = 0.01, y = 0.01, x1, x2, y1, y2;
    int N = 10000;
    FILE *fp = fopen("ans_henon_map.csv", "w");
    fprintf(fp, "x,y\n");
    x1 = x;
    y1 = y;
    for (int i = 0; i < N; i++)
    {

        x2 = y1 + 1.0 - a * x1 * x1;
        y2 = b * x1;
        fprintf(fp, "%f,%f\n", x2, y2);
        x1 = x2;
        y1 = y2;
    }

    return;
}

int main(void)
{

    henon_map();

    return 0;
}
