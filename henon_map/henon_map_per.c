#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double get_distance(double x, double y, double x2, double y2)
{
    return sqrt(pow(x - x2, 2) + pow(y - y2, 2));
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
    int M = 1000, N = 32, ans_per = 0;
    double ans_R = 0.0;
    double a_step = 2.0 / a_max, b_step = 2.0 / b_max;
    double epsilon = 0.000001;
    double target_x = 0.0, target_y = 0.0;

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
            target_x = x2; // 定常状態の最初のx座標でイプシロン近傍を定義する。
            target_y = y2; // 定常状態の最初のy座標でイプシロン近傍を定義する。
            ans_per = 0;
            // 周期性の判定を行うループ
            for (int i = 0; i < N; i++)
            {

                x2 = func01(a, x1, y1);
                y2 = func02(b, x1);

                x1 = x2;
                y1 = y2;
                ans_R = fabs(get_distance(0.0, 0.0, x2, y2));
                if (ans_R > 1000.0)
                {
                    ans_per = -1; // 原点からのユークリッド距離がr_max以上の場合は発散したと判定する。
                    break;
                }

                ans_per += 1;
                ans_R = fabs(get_distance(target_x, target_y, x2, y2));
                if (ans_R < epsilon)
                {
                    break;
                }
            }
            if (ans_R >= N)
            {
                ans_per = 0;
            }
            printf("%f,%f,%d\n", a, b, ans_per);
            fprintf(fp, "%f,%f,%d\n", a, b, ans_per);
        }
    }

    return 0;
}
