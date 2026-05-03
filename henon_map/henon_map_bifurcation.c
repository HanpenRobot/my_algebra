#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(void)
{
    double b = 0.3;

    double x = 0.01, y = 0.01, x1, x2, y1, y2;
    int N = 100000;
    FILE *fp = fopen("ans_henon_map_bifurcation.csv", "w");
    fprintf(fp, "a,x\n");
    x1 = x;
    y1 = y;
    for (double a = 0.2; a < 1.6; a += 0.01)
    {
        int M = 0;

        for (int i = 0; i < N; i++)
        {

            x2 = y1 + 1.0 - a * x1 * x1;
            y2 = b * x1;
            x1 = x2;
            y1 = y2;
            M += 1;
            if (M > 0.9 * N)
            {
                fprintf(fp, "%f,%f\n", a, x2);
            }
        }
    }

    return 0;
}
