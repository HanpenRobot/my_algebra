#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double func1(double I, double x, double y)
{

    return y + x - (pow(x, 3) / 3.0) + I;
}

double func2(double a, double b, double x, double y)
{

    return -x + a - b * y;
}

double run_runge_result(double a, double b, double I, double x0, double y0)
{
    // 4次のルンゲ・クッタ法でlotka volterra方程式を解く
    int i;
    double t = 0.0;
    double h = 0.0005; // step_size
    double x, k1, k2, k3, k4, k;
    double y, l1, l2, l3, l4, l;
    int max_step = 800000;
    double const_k = 0.2, B = 12.0;

    x = x0;
    y = y0;

    FILE *fp = fopen("ans_nagumo_eq.csv", "w");
    fprintf(fp, "t,x,y,z\n");
    for (i = 1; i < max_step; i++)
    {
        k1 = h * func1(I, x, y);
        k2 = h * func1(I, x, y + l1 / 2.0);
        k3 = h * func1(I, x, y + l2 / 2.0);
        k4 = h * func1(I, x, y + l3);
        k = (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0;
        x = x + k;

        l1 = h * func2(a, b, x, y);
        l2 = h * func2(a, b, x + k1 / 2.0, y + l1 / 2.0);
        l3 = h * func2(a, b, x + k2 / 2.0, y + l2 / 2.0);
        l4 = h * func2(a, b, x + k3, y + l3);
        l = (l1 + 2.0 * l2 + 2.0 * l3 + l4) / 6.0;
        y = y + l;

        t = t + h;
        fprintf(fp, "%f,%f,%f\n", t, x, y);
    }
    return x;
}

int main(void)
{

    double a = 3.0 / 4.0, b = 0.8, I = 2.0;
    double x0 = 3.0, y0 = 1.0; // nagumoの方程式の初期値
    run_runge_result(a, b, I, x0, y0);

    return 0;
}
