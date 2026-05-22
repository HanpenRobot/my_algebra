#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double func1(double y)
{

    return y;
}

double func2(double x, double y, double const_k, double B, double t)
{

    return -const_k * const_k - pow(x, 3) + B * cos(t);
}

double run_runge_result(double x0, double y0)
{
    // 4次のルンゲ・クッタ法でArnold方程式を解く
    int i;
    double t = 0.0;
    double h = 0.0005; // step_size
    double x, k1, k2, k3, k4, k;
    double y, l1, l2, l3, l4, l;
    int max_step = 800000;
    double const_k = 0.2, B = 12.0;

    x = x0;
    y = y0;

    FILE *fp = fopen("ans_duffing_eq.csv", "w");
    fprintf(fp, "t,x,y,z\n");
    for (i = 1; i < max_step; i++)
    {
        k1 = h * func1(y);
        k2 = h * func1(y + l1 / 2.0);
        k3 = h * func1(y + l2 / 2.0);
        k4 = h * func1(y + l3);
        k = (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0;
        x = x + k;

        l1 = h * func2(x, y, const_k, B, t);
        l2 = h * func2(x + k1 / 2.0, y + l1 / 2.0, const_k, B, t);
        l3 = h * func2(x + k2 / 2.0, y + l2 / 2.0, const_k, B, t);
        l4 = h * func2(x + k3, y + l3, const_k, B, t);
        l = (l1 + 2.0 * l2 + 2.0 * l3 + l4) / 6.0;
        y = y + l;

        t = t + h;
        fprintf(fp, "%f,%f,%f\n", t, x, y);
    }
    return x;
}

int main(void)
{

    double x0 = 3.0, y0 = 1.0; // Duffingの方程式の初期値
    run_runge_result(x0, y0);

    return 0;
}
