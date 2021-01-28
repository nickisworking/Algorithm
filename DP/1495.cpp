#include <iostream>
#include <cstring>
#include <algorithm>

#define MAX_NUM 101
#define MAX_VOLUME 1001 

using namespace std;

int v[MAX_NUM];
int dp[MAX_NUM][MAX_VOLUME];


int main() {
    int n, s, m;
    int max_val = -1;

    fill_n(v, MAX_NUM, 0);
    
    for (int i = 0; i < MAX_NUM; i++) {
        memset(dp[i], -1, sizeof(int) * MAX_VOLUME);
    }

    cin >> n >> s >> m;

    for (int i = 1; i <= n; i++) {
        cin >> v[i];
    }

    

    if (s + v[1] <= m) { dp[1][s + v[1]] = s + v[1]; }
    if (s - v[1] >= 0) { dp[1][s - v[1]] = s - v[1]; }
   
    for (int i = 1; i <= n-1; i++) {
        for (int j = 0; j <= m; j++) {
                if (dp[i][j] != -1) {
                    if (dp[i][j] + v[i + 1] <= m) { dp[i + 1][dp[i][j] + v[i + 1]] = max(dp[i + 1][dp[i][j] + v[i + 1]], dp[i][j] + v[i + 1]); }
                    if (dp[i][j] - v[i + 1] >= 0) { dp[i + 1][dp[i][j] - v[i + 1]] = max(dp[i + 1][dp[i][j] - v[i + 1]], dp[i][j] - v[i + 1]); }
                }
        }
    }

    for (int i = 0; i <= m; i++) {
        if (max_val < dp[n][i]) { max_val = dp[n][i]; }
    }

    cout << max_val;




}


