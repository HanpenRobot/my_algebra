#include <stdio.h>
#include <math.h>
#include <stdlib.h>

void henon_map(double a, int frame, FILE *fp)
{
    double b = 0.3;
    double x = 0.01, y = 0.01, x1, x2, y1, y2;
    int N = 100000;

    // fprintf(fp, "x,y\n");
    x1 = x;
    y1 = y;
    int M = 0;
    for (int i = 0; i < N; i++)
    {

        x2 = y1 + 1.0 - a * x1 * x1;
        y2 = b * x1;

        x1 = x2;
        y1 = y2;
        if (M > 0.9 * N)
        {
            fprintf(fp, "%f,%f,%lf,%d,i=%d\n", x2, y2, a, frame, i);
        }
        M += 1;
    }

    return;
}

int main(void)
{
    int frame = 0;
    FILE *fp = fopen("ans_henon_map_anim.csv", "w");
    for (double a = 0.2; a < 1.5; a += 0.01)
    {
        henon_map(a, frame, fp = fp);
        printf("%lf,frame= %d\n", a, frame);
        frame += 1;
    }

    return 0;
}
