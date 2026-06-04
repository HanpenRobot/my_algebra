#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double func1(double K1, double a, double b, double x, double y)
{

    return (K1 - a * x - b * y) * x;
}

double func2(double K2, double c, double d, double x, double y)
{

    return (K2 - c * x - d * y) * y;
}

double run_runge_result(FILE *fp, double K1, double K2, double a, double b, double c, double d, double x0, double y0, int eq_num)
{
    // 4次のルンゲ・クッタ法でlotka volterra方程式を解く
    int i;
    double t = 0.0;
    double h = 0.0005; // step_size
    double x, k1, k2, k3, k4, k;
    double y, l1, l2, l3, l4, l;
    int max_step = 40000;
    double const_k = 0.2, B = 12.0;
    printf("x0=%lf,y0=%lf\n", x0, y0);
    x = x0;
    y = y0;

    int frame_num = 0;
    for (i = 1; i < max_step; i++)
    {
        k1 = h * func1(K1, a, b, x, y);
        k2 = h * func1(K1, a, b, x, y + l1 / 2.0);
        k3 = h * func1(K1, a, b, x, y + l2 / 2.0);
        k4 = h * func1(K1, a, b, x, y + l3);
        k = (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0;
        x = x + k;

        l1 = h * func2(K2, c, d, x, y);
        l2 = h * func2(K2, c, d, x + k1 / 2.0, y + l1 / 2.0);
        l3 = h * func2(K2, c, d, x + k2 / 2.0, y + l2 / 2.0);
        l4 = h * func2(K2, c, d, x + k3, y + l3);
        l = (l1 + 2.0 * l2 + 2.0 * l3 + l4) / 6.0;
        y = y + l;

        t = t + h;
        if (i < 10 || i % 100 == 0)
        {
            fprintf(fp, "%f,%f,%f,%d,%d\n", t, x, y, frame_num, eq_num);
            frame_num += 1;
        }
    }
    return x;
}

void res_display(FILE *fp, int fnum, int A[][100], int N)
{

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            // printf("%f,%f\n", U[i][j]);
            if (j == 0)
            {
                fprintf(fp, "%d,", fnum);
            }
            if (j == N - 1)
            {
                fprintf(fp, "%d", A[i][j]);
            }
            else
            {
                fprintf(fp, "%d,", A[i][j]);
            }
        }
        fprintf(fp, "\n");
    }
}

int main()
{
    FILE *fp = fopen("ans_ca.csv", "w");
    printf("ABAAAAAAAAAAA\n");
    int N = 50;
    int U[100][100] = {0};
    int frame_num = 0;
    int f_cnt = 0;
    fprintf(fp, "n,i,j\n");
    for (int j = 0; j < N; j++)
    {
        U[j][4] = 1.0;

        U[j][7] = 1.0;
    }
    for (f_cnt = 0; f_cnt < 4; f_cnt++)
    {
        res_display(fp, frame_num, U, N);
        frame_num += 1;
        printf("f_cnt=%d", f_cnt);
        for (int i = 0; i < N; i++)
        {
            int tmpA[100] = {0};
            for (int j = 0; j < N - 1; j++)
            {
                tmpA[j] = U[i][j];
            }
            for (int j = 0; j < N - 1; j++)
            {

                if (U[i][j] == 1)
                {
                    printf("f_cnt=%d, frame_num=%d,i=%d,j=%d,A=%d\n", f_cnt, frame_num, i, j, U[i][j]);
                    // U[i][j] = 0;
                    // U[i][j + 1] = 1;
                    // U[i][j] = 0;
                    tmpA[j] = 0;
                    tmpA[j + 1] = 1;
                }
            }

            for (int j = 0; j < N - 1; j++)
            {
                U[i][j] = tmpA[j];
            }
        }
    }

    return 0;
}
