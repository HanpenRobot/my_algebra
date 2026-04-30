#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double func1(double x, double y, double z)
{
    double sigma = 10.0; // Prandtl number
    return -sigma * x + sigma * y;
}

double func2(double x, double y, double z)
{
    double R = 28.0; // Rayleigh number
    return R * x - y - x * z;
}

double func3(double x, double y, double z)
{
    double b = 8.0 / 3.0; // aspect ratio
    return -b * z + x * y;
}
double run_runge_result(double x0, double y0, double z0)
{
    // 4次のルンゲ・クッタ法でLorentz方程式を解く
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
    FILE *fp = fopen("ans_lorentz.csv", "w");
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
