#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double common_f(double alpha, double t, double s)
{
    double res = 0.0;
    res = alpha * (1.0 + exp(2 * (alpha * s + pow(alpha, 3) * t)));
    return res;
}
void run_soliton(double alpha, double t)
{
    FILE *fp = fopen("ans_soliton.csv", "w");
    fprintf(fp, "s,x,y\n");
    int max_step = 1000;
    double h = 0.05; // step_size
    double x = 0.0,
           y = 0.0, s = -10.0;

    for (int i = 0; i < max_step; i++)
    {
        double tmp_commom_denomi = common_f(alpha, t, s);
        x = s + (4.0 / tmp_commom_denomi);
        y = (-4.0 * exp(alpha * s + pow(alpha, 3) * t)) / tmp_commom_denomi;
        fprintf(fp, "%lf,%lf,%lf\n", s, x, y);
        s = s + h;
    }
}

int main(void)
{

    double alpha = 1.0, t = 0.0;
    run_soliton(alpha, t);

    return 0;
}
