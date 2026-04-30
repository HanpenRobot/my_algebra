#include <stdio.h>
#include <math.h>
#include <stdlib.h>
double c1 = -2.69, c2 = -2.383, c3 = -14.049, a1 = 0.19, a2 = -1.9644, a3 = 6.3122;

double func1(double x, double y, double z)
{
    return c1 * x + y + 0.5 * c1 * (fabsf(x - 1.0) - fabsf(x + 1.0));
}

double func2(double x, double y, double z)
{

    return c2 * x + z + 0.5 * c2 * (fabsf(x - 1.0) - fabsf(x + 1.0));
}

double func3(double x, double y, double z)
{
    return (c3 + a3) * x + a2 * y + a1 * z + 0.5 * c3 * (fabsf(x - 1.0) - fabsf(x + 1.0));
}
double run_runge_result(double x0, double y0, double z0)
{
    // 4次のルンゲ・クッタ法で区分線形連立微分方程式を解く
    int i;
    double t = 0.0;
    double h = 0.0005; // step_size
    double x, k1, k2, k3, k4, k;
    double y, l1, l2, l3, l4, l;
    double z, m1, m2, m3, m4, m;
    int max_step = 400000;

    x = x0;
    y = y0;
    z = z0;
    FILE *fp = fopen("ans_piecewise_linear.csv", "w");
    fprintf(fp, "t,x,y,z\n");
    for (i = 1; i < max_step; i++)
    {

        k1 = h * func1(x, y, z);
        k2 = h * func1(x + k1 / 2.0, y + l1 / 2.0, z + m1 / 2.0);
        k3 = h * func1(x + k2 / 2.0, y + l2 / 2.0, z + m2 / 2.0);
        k4 = h * func1(x + k3, y + l3, z + m3);
        k = (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0;
        x = x + k;

        l1 = h * func2(x, y, z);
        l2 = h * func2(x + k1 / 2.0, y + l1 / 2.0, z + m1 / 2.0);
        l3 = h * func2(x + k2 / 2.0, y + l2 / 2.0, z + m2 / 2.0);
        l4 = h * func2(x + k3, y + l3, z + m3);
        l = (l1 + 2.0 * l2 + 2.0 * l3 + l4) / 6.0;
        y = y + l;

        m1 = h * func3(x, y, z);
        m2 = h * func3(x + k1 / 2.0, y + l1 / 2.0, z + m1 / 2.0);
        m3 = h * func3(x + k2 / 2.0, y + l2 / 2.0, z + m2 / 2.0);
        m4 = h * func3(x + k3, y + l3, z + m3);
        m = (m1 + 2.0 * m2 + 2.0 * m3 + m4) / 6.0;
        z = z + m;

        t = t + h;
        fprintf(fp, "%f,%f,%f,%f\n", t, x, y, z);
    }
    return x;
}

int main(void)
{

    double x0 = 0.3, y0 = 0.0, z0 = 0.0;
    run_runge_result(x0, y0, z0);

    return 0;
}
