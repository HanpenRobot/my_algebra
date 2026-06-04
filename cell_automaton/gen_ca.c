#include <stdio.h>
#include <math.h>
#include <stdlib.h>

void res_display(FILE *fp, int fnum, int A[][100], int N)
{

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
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
    int frame_max_num = 49;
    for (f_cnt = 0; f_cnt < frame_max_num; f_cnt++)
    {
        res_display(fp, frame_num, U, N);
        frame_num += 1;
        printf("f_cnt=%d", f_cnt);
        for (int i = 1; i < N - 1; i++)
        {
            int tmpA[100][100] = {0};
            for (int ii = 0; ii < N - 1; ii++)
            {
                for (int jj = 0; jj < N - 1; jj++)
                {
                    tmpA[ii][jj] = U[i][jj];
                }
            }

            for (int j = 1; j < N - 1; j++)
            {

                if (U[i][j] == 1)
                {
                    printf("f_cnt=%d, frame_num=%d,i=%d,j=%d,A=%d\n", f_cnt, frame_num, i, j, U[i][j]);

                    tmpA[i][j] = 0;
                    tmpA[i][j + 1] = 1;
                }
            }

            for (int j = 0; j < N - 1; j++)
            {
                U[i][j] = tmpA[i][j];
            }
        }
    }

    return 0;
}
