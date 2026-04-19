#include <stdio.h>
#include <math.h>
double fnf(double x, double y)
{
    return (y - 12.0 * x + 3.0);
}

double expected_f(double t)
{
    return 12.0 * t + 9.0 - 8 * exp(t);
}

// double fnf(double t, double y)
// {
//     return (-2.0 * y);
// }

int main(void)
{
    int i;
    double t, x, h, k1, k2, k3, k4, k, res, abs_err;
    double zz;
    int N = 2000;
    printf("xの初期値を入力してください。");
    scanf("%lf", &zz);
    printf("X Y\n");
    t = 0.0;
    x = zz;
    h = 0.0001;
    for (i = 1; i < N; i++)
    {
        k1 = h * fnf(t, x);
        k2 = h * fnf(t + h / 2.0, x + k1 / 2.0);
        k3 = h * fnf(t + h / 2.0, x + k2 / 2.0);
        k4 = h * fnf(t + h, x + k3 / 2.0);
        k = (k1 + 2 * k2 + 2 * k3 + k4) / 6.0;
        t = t + h;
        x = x + k;
        res = expected_f(t);
        abs_err = fabs(res - x);
        printf("i=%d, k=%f , t=%f, x=%f, expected_f=%f, abs_err=%f\n", i, k, t, x, res, abs_err);
    }
    return 0;
}