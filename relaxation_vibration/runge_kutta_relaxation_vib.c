#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double func1(double epsilon, double v, double x)
{
    double tmp_value = epsilon * (v - (pow(v, 3) / 3.0));
    return (tmp_value - x) / v; // v=0に特異点を持つので、そこでrunge kutta法の数値積分が発散してinfとかになっている???
}

double run_runge_result(double v0, double x0)
{
    // 4次のルンゲ・クッタ法で弛緩振動の微分方程式を解く
    int i;
    double t = 0.0;
    double h = 0.0005; // step_size
    double x, v, k1, k2, k3, k4, k;

    double epsilon = 0.05;
    int max_step = 500000;

    x = x0;
    v = v0;
    FILE *fp = fopen("ans_relax.csv", "w");
    fprintf(fp, "x,v\n");
    for (i = 1; i < max_step; i++)
    {
        k1 = h * func1(epsilon, v, x);
        k2 = h * func1(epsilon, v + k1 / 2.0, x);
        k3 = h * func1(epsilon, v + k2 / 2.0, x);
        k4 = h * func1(epsilon, v + k3, x);
        k = (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0;
        x = x + h;
        v = v + k;
        fprintf(fp, "%f,%f\n", x, v);
    }
    return x;
}

int main(void)
{

    double v0 = 10.3, x0 = 1.2;
    run_runge_result(v0, x0);

    return 0;
}
