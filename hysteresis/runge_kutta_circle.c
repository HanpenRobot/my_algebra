#include <stdio.h>
#include <math.h>

double fnf(double t, double x, double A, double B)
{

    return (-pow(x, 3) + A * x - B);
}

double get_runge_result(double A, double B, double init_value)
{
    // 4次のルンゲ・クッタ法で常微分方程式を解く
    int i;
    double t, x, h, k1, k2, k3, k4, k, res;
    int max_step = 1000;

    x = init_value;
    h = 0.05; // step_size
    for (i = 1; i < max_step; i++)
    {

        k1 = h * fnf(t, x, A, B);
        k2 = h * fnf(t + h / 2.0, x + k1 / 2.0, A, B);
        k3 = h * fnf(t + h / 2.0, x + k2 / 2.0, A, B);
        k4 = h * fnf(t + h, x + k3 / 2.0, A, B);
        k = (k1 + 2 * k2 + 2 * k3 + k4) / 6.0;
        t = t + h;
        x = x + k;
        // printf("%f,%f,%f,%f\n", t, A, B, x);
    }
    return x;
}

int main(void)
{

    double A, B, init_vaule, res, R = 6.0;
    A = 10, B = 10.0;
    init_vaule = 4;
    // printf("微分方程式の初期値を入力してください。");
    // scanf("%lf", &init_vaule); // 4くらいが妥当??
    // 1. ファイルを書き込みモード("w")で開く
    FILE *fp = fopen("ans_dump_circle002.csv", "w");
    fprintf(fp, "A,B,theta,x,\n");
    int num = 0;
    for (double theta = 0; theta < 360; theta += 0.01)
    {
        A = R * cos(theta);
        B = R * sin(theta);
        // printf("theta= = %lf, init_vaule = %lf \n", theta, init_vaule);
        res = get_runge_result(A = A, B = B, init_vaule = init_vaule);
        // printf("theta= = %lf, res = %lf \n", theta, res);
        fprintf(fp, "%lf,%lf,%lf,%lf \n", A, B, theta, res);
        init_vaule = res;
        num += 1;
    }

    return 0;
}

// #include <stdio.h>

// int main() {
//     // 1. ファイルを書き込みモード("w")で開く
//     FILE *fp = fopen("example.csv", "w");
//     if (fp == NULL) {
//         printf("ファイルを開けませんでした\\n");
//         return 1;
//     }

//     // 2. CSV形式でデータを出力 (コンマ区切り)
//     fprintf(fp, "ID,Name,Age\\n");
//     fprintf(fp, "1,Tanaka,25\\n");
//     fprintf(fp, "2,Sato,30\\n");
//     fprintf(fp, "3,Suzuki,22\\n");

//     // 3. ファイルを閉じる
//     fclose(fp);
//     printf("CSVファイルを出力しました。\\n");

//     return 0;
// }