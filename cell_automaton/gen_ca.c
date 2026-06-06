#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#define N_MAX 50
#define FRAME_MAX 60

void res_display(FILE *fp, int fnum, int A[][N_MAX], int N)
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

int get_max(int *array)
{
    int ans = 0;

    for (int i = 0; i < 6; i++)
    {
        if (ans < array[i])
        {
            ans = array[i];
        }
    }
    return ans;
}

int main()
{
    FILE *fp = fopen("ans_ca.csv", "w");

    int U[N_MAX][N_MAX] = {0};
    int frame_num = 0;
    int f_cnt = 0;
    int tmpA[N_MAX][N_MAX] = {0};

    int U_history[FRAME_MAX][N_MAX][N_MAX] = {0};
    fprintf(fp, "n,i,j\n");
    for (int j = 0; j < N_MAX; j++)
    {
        U[j][4] = 1.0;

        U[j][5] = 1.0;

        if (j % 2 == 0)
        {
            U[j][10] = 1.0;

            U[j][10] = 1.0;
        }
    }
    U[25][25] = 1;
    // U[26][26] = 1;
    // U[3][3] = 1;

    for (int ii = 0; ii < N_MAX; ii++)
    {
        for (int jj = 0; jj < N_MAX; jj++)
        {
            tmpA[ii][jj] = 0;
        }
    }

    // 初回のN-1の値を保存する。
    for (int ii = 0; ii < N_MAX; ii++)
    {
        for (int jj = 0; jj < N_MAX; jj++)
        {
            U_history[0][ii][jj] = U[ii][jj];
        }
    }

    int frame_max_num = FRAME_MAX;
    for (f_cnt = 1; f_cnt < frame_max_num; f_cnt++)
    {
        res_display(fp, frame_num, U, N_MAX);
        frame_num += 1;
        printf("f_cnt=%d\n", f_cnt);

        int array[6] = {0};

        for (int ii = 0; ii < N_MAX; ii++)
        {
            for (int jj = 0; jj < N_MAX; jj++)
            {
                tmpA[ii][jj] = 0;
            }
        }
        for (int ii = 0; ii < N_MAX; ii++)
        {
            for (int jj = 0; jj < N_MAX; jj++)
            {
                tmpA[ii][jj] = U[ii][jj]; // f_cntの時の情報
                U_history[f_cnt][ii][jj] = tmpA[ii][jj];
            }
        }

        for (int i = 0; i < N_MAX; i++)
        {
            for (int j = 0; j < N_MAX; j++)
            {
                int res_local = 0;

                array[0] = tmpA[i][j];
                if (i - 1 > 0)
                {
                    array[1] = tmpA[i - 1][j];
                }
                else
                {
                    array[1] = 0;
                }
                if (i < N_MAX)
                {
                    array[2] = tmpA[i + 1][j];
                }
                else
                {
                    array[2] = 0;
                }

                if (j - 1 > 0)
                {
                    array[3] = tmpA[i][j - 1];
                }
                else
                {
                    array[3] = 0;
                }
                if (j < N_MAX)
                {
                    array[4] = tmpA[i][j + 1];
                }
                else
                {
                    array[4] = 0;
                }

                array[5] = U_history[f_cnt - 1][i][j];
                res_local = get_max(array) - U_history[f_cnt - 1][i][j];

                U[i][j] = res_local; // f_cntがf_cnt+1の時の情報に更新される
            }
        }
    }

    return 0;
}
