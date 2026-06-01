#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double get_distance(double x, double y, double x2, double y2)
{
    return sqrt(pow(x - x2, 2) + pow(y - y2, 2));
}
int get_period(double *tmpA1, double *tmpA2, double targetA1, double targetA2)
{
    double res = 0.0;
    double epsilon = 0.000001;
    int i = 0;
    int max_period = 32;
    double r_max = 1000.0;
    for (i = 0; i < max_period; i++)
    {

        res = fabs(get_distance(tmpA1[i], tmpA2[i], targetA1, targetA2));
        if (res < epsilon)
        {
            return i;
        }
    }
    return -1; // 周期がmax_period以上の場合も発散したと判定する。
}

double func01(double a, double x, double y)
{
    return y + 1.0 - a * x * x;
}

double func02(double b, double x)
{
    return b * x;
}

int main(void)
{
    int a_max = 640, b_max = 480;
    double x = 0.01, y = 0.01, x1, x2, y1, y2;
    int M = 4000, N = 32, ans_per = 0;
    double ans_R = 0.0;
    double a_step = 2.0 / a_max, b_step = 2.0 / b_max;
    double A1[100] = {0.0}, A2[100] = {0.0};

    FILE *fp = fopen("ans_henon_map_per.csv", "w");
    fprintf(fp, "a,b,per\n");

    for (double a = 0.0; a <= 2.0; a += a_step)
    {

        for (double b = -1.0; b <= 1.0; b += b_step)
        {
            x1 = x;
            y1 = y;
            for (int i = 0; i < M; i++)
            {

                x2 = func01(a, x1, y1);
                y2 = func02(b, x1);
                x1 = x2;
                y1 = y2;
            }
            // 周期性の判定を行うループ
            for (int i = 0; i < N; i++)
            {

                x2 = func01(a, x1, y1);
                y2 = func02(b, x1);
                A1[i] = x2;
                A2[i] = y2;
                x1 = x2;
                y1 = y2;
                ans_R = fabs(get_distance(0.0, 0.0, x2, y2));
                if (ans_R > 1000.0)
                {
                    ans_per = -1; // 原点からのユークリッド距離がr_max以上の場合は発散したと判定する。
                }

                ans_per = get_period(A1, A2, x2, y2);
            }
            printf("%f,%f,%d\n", a, b, ans_per);
            fprintf(fp, "%f,%f,%d\n", a, b, ans_per);
        }
    }

    return 0;
}
