#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

long long graph[2][5004][5004];
long long a[5004];
int n;          
int main()
{
    cin >> n;
    for(int i = 0;i<n;++i) {
        cin >> a[i];
        graph[1][0][i] = 1000000000;
    }
    graph[1][0][0] = 1000000000;
    graph[1][0][n] = 1000000000;
    for (int i=1; i<=(n/2 + (n%2)); i++){
        for(int j=0; j<=i; j++){
            graph[1][i][j] = 1000000000;
            graph[0][i][j] = 1000000000;
      }
    }
    graph[1][1][1] = 0;
    graph[1][0][n] = 1000000000;
    graph[0][0][0] = 0;
    for (int i=1; i<=(n/2+(n%2)); i++){
      for (int j=i+1; j<=n; j++){
        long long b = max(0ll, a[j-1] - a[j-2] + 1);
        long long c = graph[1][i][j-1];
        long long d = graph[0][i][j-1];
        long long e = c + b;
        graph[0][i][j] = min(d, c+b);
        long long h = max(0ll, a[j-2] - a[j-1] + 1);
        long long u = graph[0][i-1][j-2];
        long long k = max(0ll, a[j-2]-min(a[j-1], a[j-3])+1);
        long long p = graph[1][i-1][j-2];
        graph[1][i][j] = min(u+h, p+k);
      }
    }
    for (int i=1; i<=(n/2+(n%2)); i++){
        long long o = min(graph[0][i][n], graph[1][i][n]);
        cout << o << " ";
    }
    return 0;
}
