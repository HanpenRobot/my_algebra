#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double func1(double x, double y)
{
    return y;
}

double func2(double x, double y)
{

    return -x / pow(x, 3);
}

// double func3(double E, double x, double y, double z, double w)
// {
//     return y;
// }
// double func4(double E, double x, double y, double z, double w)
// {
//     return -z * (pow(z, 2) + E * pow(w, 2));
// }
double run_runge_result(double x0, double y0)
{
    // 4次のルンゲ・クッタ法でニュートン中心力系の微分方程式を解く
    int i;
    double t = 0.0;
    double h = 0.0005; // step_size
    double x, k1, k2, k3, k4, k;
    double y, l1, l2, l3, l4, l;
    // double z, m1, m2, m3, m4, m;
    // double w, n1, n2, n3, n4, n;

    int max_step = 800000;

    x = x0;
    y = y0;
    // z = z0;
    FILE *fp = fopen("ans_grad.csv", "w");
    fprintf(fp, "t,x,v\n");
    for (i = 1; i < max_step; i++)
    {
        k1 = h * func1(x, y);
        k2 = h * func1(x + k1 / 2.0, y + l1 / 2.0);
        k3 = h * func1(x + k2 / 2.0, y + l2 / 2.0);
        k4 = h * func1(x + k3, y + l3);
        k = (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0;
        x = x + k;

        l1 = h * func2(x, y);
        l2 = h * func2(x + k1 / 2.0, y + l1 / 2.0);
        l3 = h * func2(x + k2 / 2.0, y + l2 / 2.0);
        l4 = h * func2(x + k3, y + l3);
        l = (l1 + 2.0 * l2 + 2.0 * l3 + l4) / 6.0;
        y = y + l;

        // m1 = h * func3(E, x, y, z, w);
        // m2 = h * func3(E, x + k1 / 2.0, y + l1 / 2.0, z + m1 / 2.0, w + n1 / 2.0);
        // m3 = h * func3(E, x + k2 / 2.0, y + l2 / 2.0, z + m2 / 2.0, w + n2 / 2.0);
        // m4 = h * func3(E, x + k3, y + l3, z + m3, w + n3);
        // m = (m1 + 2.0 * m2 + 2.0 * m3 + m4) / 6.0;
        // z = z + m;

        // n1 = h * func1(E, x, y, z, w);
        // n2 = h * func1(E, x + k1 / 2.0, y + l1 / 2.0, z + m1 / 2.0, w + n1 / 2.0);
        // n3 = h * func1(E, x + k2 / 2.0, y + l2 / 2.0, z + m2 / 2.0, w + n2 / 2.0);
        // n4 = h * func1(E, x + k3, y + l3, z + m3, w + n3);
        // n = (n1 + 2.0 * n2 + 2.0 * n3 + n4) / 6.0;
        // w = w + n;

        t = t + h;
        if (i < 10 || i % 300 == 0)
        {
            fprintf(fp, "%f,%f,%f\n", t, x, y);
        }
    }
    return x;
}

int main(void)
{

    double x0 = 3.0, y0 = 0.0;
    run_runge_result(x0, y0);

    return 0;
}
