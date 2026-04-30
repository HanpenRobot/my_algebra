#include <stdio.h>
#include <math.h>
#include <stdlib.h>
double epsilon = 0.3, omega = 140.0;

double func1(double theta1, double theta2)
{
    double ans = 150.0 + epsilon * sin(theta2 - theta1);

    return ans;
}

double func2(double theta1, double theta2)
{
    double ans = 150.0 + epsilon * sin(theta1 - theta2);
    return ans;
}

void run_runge_result(double theta1_0, double theta2_0)
{
    // 4次のルンゲ・クッタ法で同期現象(蔵元モデル)の微分方程式を解く
    int i;
    double t = 0.0;
    double h = 0.0005; // step_size
    double theta1, k1, k2, k3, k4, k;
    double theta2, l1, l2, l3, l4, l;

    int max_step = 400000;

    theta1 = theta1_0;
    theta2 = theta2_0;
    FILE *fp = fopen("ans_sync_phenom.csv", "w");
    fprintf(fp, "t,x,y\n", t, theta1, theta2);
    for (i = 1; i < max_step; i++)
    {

        k1 = h * func1(theta1, theta2);
        k2 = h * func1(theta1 + k1 / 2.0, theta2 + l1 / 2.0);
        k3 = h * func1(theta1 + k2 / 2.0, theta2 + l2 / 2.0);
        k4 = h * func1(theta1 + k3, theta2 + l3);
        k = (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0;
        theta1 = theta1 + k;

        l1 = h * func2(theta1, theta2);
        l2 = h * func2(theta1 + k1 / 2.0, theta2 + l1 / 2.0);
        l3 = h * func2(theta1 + k2 / 2.0, theta2 + l2 / 2.0);
        l4 = h * func2(theta1 + k3, theta2 + l3);
        l = (l1 + 2.0 * l2 + 2.0 * l3 + l4) / 6.0;
        theta2 = theta2 + l;

        t = t + h;
        fprintf(fp, "%f,%f,%f\n", t, theta1, theta2);
    }
    return;
}

int main(void)
{

    // double theta1_0 = 0.0, theta2_0 = 3.0;
    double theta1_0 = 1.0, theta2_0 = 0.0;
    run_runge_result(theta1_0, theta2_0);

    return 0;
}
