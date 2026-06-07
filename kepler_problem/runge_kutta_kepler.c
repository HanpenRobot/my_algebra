#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double run_kepler(double c, double k, double A, double B)
{
    FILE *fp = fopen("ans_kepler.csv", "w");
    fprintf(fp, "phi,x,y\n");
    int max_step = 500;
    double x = 0.0, y = 0.0, r = 0.0, phi = 0.0, rho = 0.0;
    double p, e;
    double h = 0.05; // step_size
    p = pow(c, 2) / k;
    e = pow(c, 2) * sqrt(pow(A, 2) + pow(B, 2)) / k;
    for (int i = 0; i < max_step; i++)
    {
        rho = A * cos(phi) + B * sin(phi) + (k / (pow(c, 2)));
        r = 1.0 / rho;
        phi = phi + h;
        x = r * cos(phi);
        y = r * sin(phi);
        fprintf(fp, "%lf,%lf,%lf\n", phi, x, y);
    }
}

int main(void)
{

    double c = 1.0, k = 1.0, A = 0.63, B = 0.63;
    run_kepler(c, k, A, B);

    return 0;
}
