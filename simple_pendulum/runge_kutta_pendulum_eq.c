#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double func1(double x, double y)
{

    return y;
}

double func2(double a, double x, double y)
{

    return -a * sin(x);
}

double run_runge_result(FILE *fp, double a, double x0, double y0, int eq_num)
{
    // 4次のルンゲ・クッタ法で単振り子の方程式を解く
    int i;
    double t = 0.0;
    double h = 0.0005; // step_size
    double x, k1, k2, k3, k4, k;
    double y, l1, l2, l3, l4, l;
    int max_step = 40000;
    double const_k = 0.2, B = 12.0;
    printf("x0=%lf,y0=%lf\n", x0, y0);
    x = x0;
    y = y0;

    int frame_num = 0;
    for (i = 1; i < max_step; i++)
    {
        k1 = h * func1(x, y);
        k2 = h * func1(x, y + l1 / 2.0);
        k3 = h * func1(x, y + l2 / 2.0);
        k4 = h * func1(x, y + l3);
        k = (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0;
        x = x + k;

        l1 = h * func2(a, x, y);
        l2 = h * func2(a, x + k1 / 2.0, y + l1 / 2.0);
        l3 = h * func2(a, x + k2 / 2.0, y + l2 / 2.0);
        l4 = h * func2(a, x + k3, y + l3);
        l = (l1 + 2.0 * l2 + 2.0 * l3 + l4) / 6.0;
        y = y + l;

        t = t + h;
        if (i < 10 || i % 100 == 0)
        {
            fprintf(fp, "%f,%f,%f,%d,%d\n", t, x, y, frame_num, eq_num);
            frame_num += 1;
        }
    }
    return x;
}

int main(void)
{
    FILE *fp = fopen("ans_simple_pendulum_eq.csv", "w");
    fprintf(fp, "t,x,y,z\n");
    double a = 2.0;

    int eq_num = 0;
    for (double x0 = -10.0; x0 < 10.0; x0 += 0.5)
        for (double y0 = -8.0; y0 < 8.0; y0 += 0.5)
        {
            {
                run_runge_result(fp, a, x0, y0, eq_num);
                // printf("x0=%lf,y0=%lf\n", x0, y0);
                eq_num += 1;
            }
        }

    return 0;
}
