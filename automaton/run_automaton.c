#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#define M_MAX 100000
void run_automaton()
{
    int N = 1000;
    int T = 1000;
    FILE *fp = fopen("ans_automaton.csv", "w");

    int A[M_MAX] = {0};
    int A2[M_MAX] = {0};
    for (int i = 0; i < N; i++)
    {
        A[i] = 0;
        A2[i] = 0;
    }
    A[0] = 1;
    for (int t = 0; t < T; t++)
    {
        for (int i = 0; i < N; i++)
        {
            if (i == (N - 1))
            {
                fprintf(fp, "%d", A[i]);
            }
            else
            {
                fprintf(fp, "%d,", A[i]);
            };
        }
        for (int i = 0; i < N; i++)
        {
            A2[i] = A[i];
        }
        for (int i = 0; i < N; i++)
        {
            if (i == 0)
            {
                continue;
            }
            if (i == (N - 1))
            {
                continue;
            }
            A[i] = (A2[i - 1] + A2[i + 1]) % 2;
        }

        fprintf(fp, "\n");
    }
}

void run_automaton2()
{
    int N = 1000;
    int T = 1000;
    FILE *fp = fopen("ans_automaton2.csv", "w");

    int A[M_MAX] = {0};
    int A2[M_MAX] = {0};
    for (int i = 0; i < N; i++)
    {
        A[i] = 0;
        A2[i] = 0;
    }
    A[0] = 1;
    for (int t = 0; t < T; t++)
    {
        for (int i = 0; i < N; i++)
        {
            if (A[i] == 0)
            {
                fprintf(fp, "□");
            }
            if (A[i] == 1)
            {
                fprintf(fp, "■");
            }
        }
        for (int i = 0; i < N; i++)
        {
            A2[i] = A[i];
        }
        for (int i = 0; i < N; i++)
        {
            if (i == 0)
            {
                continue;
            }
            if (i == (N - 1))
            {
                continue;
            }
            A[i] = (A2[i - 1] + A2[i + 1]) % 2;
        }

        fprintf(fp, "\n");
    }
}

void run_automaton_pos()
{
    int N = 1000;
    int T = 1000;
    FILE *fp = fopen("ans_automaton_pos.csv", "w");

    int A[M_MAX] = {0};
    int A2[M_MAX] = {0};
    for (int i = 0; i < N; i++)
    {
        A[i] = 0;
        A2[i] = 0;
    }
    A[0] = 1;

    for (int t = 0; t < T; t++)
    {
        for (int i = 0; i < N; i++)
        {

            if (A[i] == 1)
            {

                fprintf(fp, "%d,%d\n", i, t);
            }
        }
        for (int i = 0; i < N; i++)
        {
            A2[i] = A[i];
        }
        for (int i = 0; i < N; i++)
        {
            if (i == 0)
            {
                continue;
            }
            if (i == (N - 1))
            {
                continue;
            }
            A[i] = (A2[i - 1] + A2[i + 1]) % 2;
        }
    }
}

int main(void)
{
    run_automaton2();

    return 0;
}
