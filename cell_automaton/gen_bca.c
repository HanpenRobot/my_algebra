#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#define N_MAX 50
#define FRAME_MAX 30

void res_display(FILE *fp, int f_cnt, int A[][N_MAX], int N)
{

    for (int i = -1; i < N; i++)
    {
        if (i == -1)
        {
            fprintf(fp, "%d,", f_cnt);
        }
        if (i == N - 1)
        {
            fprintf(fp, "%d", A[f_cnt][i]);
        }
        else
        {
            fprintf(fp, "%d,", A[f_cnt][i]);
        }
    }
    fprintf(fp, "\n");
}

int main()
{
    FILE *fp = fopen("ans_bca.csv", "w");
    int U[FRAME_MAX][N_MAX] = {0};
    int tmpU[N_MAX] = {0};
    int tmpU2[N_MAX] = {0};
    int tmpU3[N_MAX] = {0};
    int frame_num = 0;
    U[0][3] = 1;
    // U[0][5] = 1;
    fprintf(fp, "t,j\n");

    for (int f_cnt = 1; f_cnt < FRAME_MAX; f_cnt++)
    {
        for (int i = 0; i < N_MAX; i++)
        {
            tmpU[i] = U[f_cnt - 1][i];
            tmpU2[i] = 0;
        }
        for (int j = 1; j < N_MAX - 1; j++)
        {

            if (tmpU[j - 1] == 0 && tmpU[j] == 0 && tmpU[j + 1] == 0)
            {
                tmpU2[j] = 0;
            }

            if (tmpU[j - 1] == 0 && tmpU[j] == 0 && tmpU[j + 1] == 1)
            {
                tmpU2[j] = 0;
            }

            if (tmpU[j - 1] == 0 && tmpU[j] == 1 && tmpU[j + 1] == 0)
            {
                tmpU2[j] = 0;
            }

            if (tmpU[j - 1] == 0 && tmpU[j] == 1 && tmpU[j + 1] == 1)
            {
                tmpU2[j] = 1;
            }
            if (tmpU[j - 1] == 1 && tmpU[j] == 0 && tmpU[j + 1] == 0)
            {
                tmpU2[j] = 1;
            }
            if (tmpU[j - 1] == 1 && tmpU[j] == 0 && tmpU[j + 1] == 1)
            {
                tmpU2[j] = 1;
            }
            if (tmpU[j - 1] == 1 && tmpU[j] == 1 && tmpU[j + 1] == 0)
            {
                tmpU2[j] = 0;
            }
            if (tmpU[j - 1] == 1 && tmpU[j] == 1 && tmpU[j + 1] == 1)
            {
                tmpU2[j] = 1;
            }
        }
        for (int j = 0; j < N_MAX; j++)
        {

            U[f_cnt][j] = tmpU2[j];
        }

        res_display(fp, f_cnt, U, N_MAX);
    }

    return 0;
}
