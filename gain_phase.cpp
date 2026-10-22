#include <cstdio>
#include <complex>

double func(double omega)
{
    // double omega_r = 50, omega_r2;
    double B = sqrt(2) / 2.0;
    double k1 = 0.04, k2 = 1.0;

    // omega_r2 = pow(omega_r, 2);
    std::complex<double>
        tmp_s, A, A2, A3, p, omega_r, omega_r2, tmp_ans;
    ;
    tmp_s = std::complex<double>(0, omega);
    A = std::complex<double>(1000, 0);
    A2 = std::complex<double>(27, 0);
    A3 = std::complex<double>(28, 0);
    omega_r = std::complex<double>(50, 0);
    omega_r2 = std::complex<double>(pow(50, 2), 0);
    p = (tmp_s + A) * (tmp_s + A2) * (tmp_s + A3);
    tmp_ans = (omega_r2 * p) / ((k1 * tmp_s + k2) * (pow(tmp_s, 2) + 2.0 * B * tmp_s + omega_r2));

    return 20.0 * log10((tmp_ans.real(), 2) + pow(tmp_ans.imag(), 2));
}
int main()
{

    int num;

    double s = 0.0;
    double x = 1.0;
    double ans = 0.0;
    for (x = 0.1; x < 4.1; x += 0.04)
    {
        s = pow(10, x);
        ans = func(s);
        std::printf("s=%f ,ans=%f\n", s, ans);
    }

    return 0;
}
