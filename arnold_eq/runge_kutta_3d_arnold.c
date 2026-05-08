#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double func1(double A, double B, double C, double x, double y, double z)
{

    return A * sin(z) + C * cos(y);
}

double func2(double A, double B, double C, double x, double y, double z)
{

    return B * sin(x) + A * cos(z);
}

double func3(double A, double B, double C, double x, double y, double z)
{
    return C * sin(y) + B * cos(x);
}
double run_runge_result(double x0, double y0, double z0)
{
    // 4次のルンゲ・クッタ法でArnold方程式を解く
    int i;
    double t = 0.0;
    double h = 0.0005; // step_size
    double x, k1, k2, k3, k4, k;
    double y, l1, l2, l3, l4, l;
    double z, m1, m2, m3, m4, m;
    int max_step = 800000;
    double A = 1.0, B = 0.5, C = 0.3;

    x = x0;
    y = y0;
    z = z0;
    FILE *fp = fopen("ans_arnold2.csv", "w");
    fprintf(fp, "t,x,y,z\n");
    for (i = 1; i < max_step; i++)
    {
        k1 = h * func1(A, B, C, x, y, z);
        k2 = h * func1(A, B, C, x + k1 / 2.0, y + l1 / 2.0, z + m1 / 2.0);
        k3 = h * func1(A, B, C, x + k2 / 2.0, y + l2 / 2.0, z + m2 / 2.0);
        k4 = h * func1(A, B, C, x + k3, y + l3, z + m3);
        k = (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0;
        x = x + k;

        l1 = h * func2(A, B, C, x, y, z);
        l2 = h * func2(A, B, C, x + k1 / 2.0, y + l1 / 2.0, z + m1 / 2.0);
        l3 = h * func2(A, B, C, x + k2 / 2.0, y + l2 / 2.0, z + m2 / 2.0);
        l4 = h * func2(A, B, C, x + k3, y + l3, z + m3);
        l = (l1 + 2.0 * l2 + 2.0 * l3 + l4) / 6.0;
        y = y + l;

        m1 = h * func3(A, B, C, x, y, z);
        m2 = h * func3(A, B, C, x + k1 / 2.0, y + l1 / 2.0, z + m1 / 2.0);
        m3 = h * func3(A, B, C, x + k2 / 2.0, y + l2 / 2.0, z + m2 / 2.0);
        m4 = h * func3(A, B, C, x + k3, y + l3, z + m3);
        m = (m1 + 2.0 * m2 + 2.0 * m3 + m4) / 6.0;
        z = z + m;

        t = t + h;
        fprintf(fp, "%f,%f,%f,%f\n", t, x, y, z);
    }
    return x;
}

int main(void)
{

    // double x0 = 3.0, y0 = 0.0, z0 = 3.0; // 軌道がカオス的になる初期値
    double x0 = 4.2, y0 = 0.0, z0 = 3.0; // 軌道がトーラス状になる初期値
    run_runge_result(x0, y0, z0);

    return 0;
}
