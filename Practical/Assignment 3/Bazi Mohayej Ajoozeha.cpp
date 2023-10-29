#include<bits/stdc++.h>

using namespace std;

int Moraba2(int i);
int Moraba3(int i);
int Moraba(int i);
long bishopPlace(int n, int k);
int main(){
	int n, k;
    cin >> n >> k;
	long output = bishopPlace(n, k);
	cout << (output);
}
int Moraba2(int i){
    return i / 4 * 2 + 1;}
int Moraba3(int i){
    return (i-1) / 4 * 2 + 2;}
int Moraba(int i){
	if ((i & 1) == 1)
		return Moraba2(i);
	else
		return Moraba3(i);}
long bishopPlace(int n, int k){
    long dynomic[n * 2][k + 1];
    long output = 0;
    int nk = 2 * n - 1;
	if (k > nk){
        return 0;}
	for(int i = 0; i < n * 2; i++){
		for(int j = 0; j < k + 1; j++){
			dynomic[i][j] = 0;}
            dynomic[i][0] = 1;}	
	dynomic[1][1] = 1;
	for (int i = 2; i < n * 2; i++){
		for (int j = 1; j <= k; j++){
            long t = dynomic[i - 2][j - 1];
            long s = (Moraba(i) - j + 1);
            long p = dynomic[i - 2][j];
            long r = t * s;
			dynomic[i][j] = p + r;}}
	for (int i = 0; i <= k; i++){
        long y = dynomic[n * 2 - 1][i];
        long u = dynomic[n * 2 - 2][k - i];
		output = output + y * u;}
	return output;
}
