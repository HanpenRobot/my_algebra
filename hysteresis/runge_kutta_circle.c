#include <stdio.h>
#include <math.h>

double fnf(double t, double x, double A, double B)
{

    return (-pow(x, 3) - A * x - B);
}

double get_runge_result(double A, double B, double init_value)
{
    // 4次のルンゲ・クッタ法で常微分方程式を解く
    int i;
    double t, x, h, k1, k2, k3, k4, k, res;
    int max_step = 1000;

    x = init_value;
    h = 0.05; // step_size
    for (i = 1; i < max_step; i++)
    {

        k1 = h * fnf(t, x, A, B);
        k2 = h * fnf(t + h / 2.0, x + k1 / 2.0, A, B);
        k3 = h * fnf(t + h / 2.0, x + k2 / 2.0, A, B);
        k4 = h * fnf(t + h, x + k3 / 2.0, A, B);
        k = (k1 + 2 * k2 + 2 * k3 + k4) / 6.0;
        t = t + h;
        x = x + k;
        printf("%f,%f,%f,%f\n", t, A, B, x);
    }
    return x;
}

int main(void)
{

    double A, B, init_vaule, res;
    A = 2, B = 0.0;
    printf("微分方程式の初期値を入力してください。");
    scanf("%lf", &init_vaule); // 4くらいが妥当??
    res = get_runge_result(A = A, B = B, init_vaule = init_vaule);
    printf("res = %lf", res);
    return 0;
}