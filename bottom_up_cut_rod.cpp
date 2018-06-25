#include <iostream>

using namespace std;

int bottom_up_cut_rod(int* p, int n)
{
    int dp[n + 1];
    dp[0] = 0;
    for (int j = 1; j <= n; j++)
    {
        int q = 0x80000000;
        for (int i = 1; i <= j; ++i)
        {
            q = max(q, p[i-1] + dp[j - i]);
        }
        dp[j] = q;
    }
    return dp[n];
}

int main()
{
    int p[10] = {1, 5, 8, 9, 10, 17, 17, 20, 24, 30};
    int n;
    cin >> n;
    int result = bottom_up_cut_rod(p, n);
    cout << result << endl;
    return 0;
}
