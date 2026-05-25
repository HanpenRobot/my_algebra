#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double func1(double K1, double a, double b, double x, double y)
{

    return (K1 - a * x - b * y) * x;
}

double func2(double K2, double c, double d, double x, double y)
{

    return (K2 - c * x - d * y) * y;
}

double run_runge_result(FILE *fp, double K1, double K2, double a, double b, double c, double d, double x0, double y0, int eq_num)
{
    // 4次のルンゲ・クッタ法でlotka volterra方程式を解く
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
        k1 = h * func1(K1, a, b, x, y);
        k2 = h * func1(K1, a, b, x, y + l1 / 2.0);
        k3 = h * func1(K1, a, b, x, y + l2 / 2.0);
        k4 = h * func1(K1, a, b, x, y + l3);
        k = (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0;
        x = x + k;

        l1 = h * func2(K2, c, d, x, y);
        l2 = h * func2(K2, c, d, x + k1 / 2.0, y + l1 / 2.0);
        l3 = h * func2(K2, c, d, x + k2 / 2.0, y + l2 / 2.0);
        l4 = h * func2(K2, c, d, x + k3, y + l3);
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
    FILE *fp = fopen("ans_lotka_volterra_eq4.csv", "w");
    fprintf(fp, "t,x,y,z\n");
    // double a = 2.0, b = 1.0, c = 1.0, d = 3.0, K1 = 6.0, K2 = 5.0;
    double a = 1.0, b = 3.0, c = 2.0, d = 1.0, K1 = 5.0, K2 = 6.0;
    // (K1 / a) < (K2 / c) and (K2 / d) < (K2 / b) -> (x,y) neq (0,0)となる平衡点を持つ
    //(6.0 / 2) < (10 / 2) and (10 / 6) < (6 / 3 )
    // double x0 = 0.5, y0 = 0.5; // lotka_volterraの方程式の初期値
    //  run_runge_result(fp, K1, K2, a, b, c, d, x0, y0);

    int eq_num = 0;
    // x0 = 0.3, y0 = 0.3; // lotka_volterraの方程式の初期値
    for (double x0 = 0.0; x0 < 15.0; x0 += 0.5)
        for (double y0 = 0.0; y0 < 15.0; y0 += 0.5)
        {
            {
                run_runge_result(fp, K1, K2, a, b, c, d, x0, y0, eq_num);
                // printf("x0=%lf,y0=%lf\n", x0, y0);
                eq_num += 1;
            }
        }

    // x0 = 5.0, y0 = 10.0; // lotka_volterraの方程式の初期値
    // run_runge_result(fp, K1, K2, a, b, c, d, x0, y0);

    return 0;
}
