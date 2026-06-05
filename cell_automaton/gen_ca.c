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

int get_max(int *array)
{
    int ans = 0;

    for (int i = 0; i < 6; i++)
    {
        // printf("array[%d]=%d\n", i, array[i]);
        if (ans < array[i])
        {
            ans = array[i];
        }
    }
    return ans;
}

// int main()
// {
//     int tmp_array[5] = {0};
//     int res = 0;
//     tmp_array[0] = -3;
//     tmp_array[1] = 2;
//     tmp_array[2] = 1;
//     res = get_max(tmp_array);

//     printf("res=%d\n", res);
//     return 0;
// }

// int main()
// {
//     int tmp_array[10] = {0};
//     int tmp_array_before[10] = {0};
//     for (int i = 0; i < 10; i++)
//     {
//         tmp_array[i] = i + 1;
//     }
//     for (int i = 0; i < 10; i++)
//     {
//         if (i > 1)
//         {
//             tmp_array_before[i] = tmp_array[i - 1];
//             printf("tmp_array[%d]=%d , tmp_array_before[%d]=%d \n ", i, tmp_array[i], i, tmp_array_before[i]);
//         }
//         else
//         {
//             printf("tmp_array[%d]=%d \n ", i, tmp_array[i]);
//         }
//     }
//     // int res = 0;
//     // tmp_array[0] = -3;
//     // tmp_array[1] = 2;
//     // tmp_array[2] = 1;
//     // res = get_max(tmp_array);

//     // printf("res=%d\n", res);
//     return 0;
// }

int main()
{
    FILE *fp = fopen("ans_ca.csv", "w");

    int N = 50;
    int U[100][100] = {0};
    int frame_num = 0;
    int f_cnt = 0;
    int tmpA_before[100][100] = {0};
    int tmpA[100][100] = {0};
    int tmpA2[100][100] = {0};
    int tmpA3[100][100] = {0};
    int tmpA4[100][100] = {0};
    int U_history[10][100][100] = {0};
    fprintf(fp, "n,i,j\n");
    for (int j = 0; j < N; j++)
    {
        U[j][4] = 1.0;

        U[j][5] = 1.0;

        if (j % 2 == 0)
        {
            U[j][10] = 1.0;

            U[j][10] = 1.0;
        }
    }

    for (int ii = 0; ii < 100; ii++)
    {
        for (int jj = 0; jj < 100; jj++)
        {
            tmpA_before[ii][jj] = 0;
            tmpA[ii][jj] = 0;
            tmpA2[ii][jj] = 0;
        }
    }

    // 初回のN-1の値を保存する。
    for (int ii = 0; ii < N; ii++)
    {
        for (int jj = 0; jj < N; jj++)
        {
            tmpA_before[ii][jj] = U[ii][jj];
            tmpA2[ii][jj] = U[ii][jj];
            tmpA3[ii][jj] = U[ii][jj];
            tmpA4[ii][jj] = U[ii][jj];
            U_history[0][ii][jj] = U[ii][jj];
        }
    }

    int frame_max_num = 20;
    for (f_cnt = 1; f_cnt < frame_max_num; f_cnt++)
    {
        res_display(fp, frame_num, U, N);
        frame_num += 1;
        printf("f_cnt=%d\n", f_cnt);

        int array[6] = {0};

        for (int ii = 0; ii < 100; ii++)
        {
            for (int jj = 0; jj < 100; jj++)
            {
                tmpA[ii][jj] = 0;
                // tmpA2[ii][jj] = 0;
                // tmpA3[ii][jj] = 0;
            }
        }
        for (int ii = 0; ii < N; ii++)
        {
            for (int jj = 0; jj < N; jj++)
            {
                tmpA[ii][jj] = U[ii][jj]; // f_cntの時の情報
                U_history[f_cnt][ii][jj] = tmpA[ii][jj];
                // tmpA2[ii][jj] = U[ii][jj];
                // tmpA3[ii][jj] = tmpA[ii][jj];
            }
        }
        // for (int ii = 0; ii < N; ii++)
        // {
        //     for (int jj = 0; jj < N; jj++)
        //     {
        //         U_history[f_cnt][ii][jj] = tmpA[ii][jj]; // f_cntの時の情報　(どうやったらf_cnt-1の情報を保存できるか?)
        //         // tmpA2[ii][jj] = U[ii][jj];
        //         // tmpA3[ii][jj] = tmpA[ii][jj];
        //     }
        // }
        for (int i = 1; i < N - 1; i++)
        {
            for (int j = 1; j < N - 1; j++)
            {
                int res_local = 0;
                array[0] = tmpA[i][j];
                array[1] = tmpA[i - 1][j];
                array[2] = tmpA[i + 1][j];
                array[3] = tmpA[i][j - 1];
                array[4] = tmpA[i][j + 1];
                array[5] = U_history[f_cnt - 1][i][j];
                res_local = get_max(array) - U_history[f_cnt - 1][i][j];
                // if (f_cnt > 1)
                // {
                //     array[5] = U_history[f_cnt - 2][i][j];
                //     res_local = get_max(array) - U_history[f_cnt - 2][i][j];
                // }
                // else
                // {
                //     array[5] = tmpA[i][j + 1];
                //     res_local = get_max(array);
                // }

                U[i][j] = res_local; // f_cntがf_cnt+1の時の情報に更新される
            }
        }

        //     for (int i = 1; i < N - 1; i++)
        //     {

        //         int array[6] = {0};
        //         for (int ii = 0; ii < N; ii++)
        //         {
        //             for (int jj = 0; jj < N; jj++)
        //             {
        //                 tmpA[ii][jj] = U[i][jj];
        //             }
        //         }

        //         for (int j = 1; j < N - 1; j++)
        //         {

        //             // if (U[i][j] == 1)
        //             // {
        //             //     int res_local = 0;
        //             //     array[0] = tmpA[i][j];
        //             //     array[1] = tmpA[i + 1][j];
        //             //     array[2] = tmpA[i - 1][j];
        //             //     array[3] = tmpA[i][j - 1];
        //             //     array[4] = tmpA[i][j + 1];
        //             //     array[5] = tmpA_before[i][j];
        //             //     res_local = get_max(array) - tmpA_before[i][j];
        //             //     tmpA[i][j] = res_local - tmpA_before[i][j];
        //             //     printf("f_cnt=%d, frame_num=%d,i=%d,j=%d,A=%d,res_max=%d\n", f_cnt, frame_num, i, j, U[i][j], res_local);
        //             //     // tmpA[i][j] = 0;
        //             //     // tmpA[i][j + 1] = 1;
        //             // }
        //             int res_local = 0;
        //             array[0] = tmpA[i][j - 1];
        //             array[1] = tmpA[i][j - 1];
        //             array[2] = tmpA[i][j + 1];
        //             array[3] = tmpA[i][j + 1];
        //             array[4] = tmpA[i][j];
        //             array[5] = tmpA2[i][j];
        //             res_local = get_max(array);
        //             tmpA[i][j] = res_local - tmpA2[i][j];
        //             // printf("f_cnt=%d, frame_num=%d,i=%d,j=%d,A=%d,res_max=%d\n", f_cnt, frame_num, i, j, U[i][j], res_local);
        //         }

        //         for (int j = 0; j < N - 1; j++)
        //         {
        //             U[i][j] = tmpA[i][j];
        //         }
        //         if (f_cnt > 0)
        //         {
        //             for (int ii = 0; ii < N; ii++)
        //             {
        //                 for (int jj = 0; jj < N; jj++)
        //                 {
        //                     // tmpA[ii][jj] = U[ii][jj];
        //                     tmpA2[ii][jj] = U[ii][jj];
        //                 }
        //             }
        //         }
        //     }
    }

    return 0;
}
