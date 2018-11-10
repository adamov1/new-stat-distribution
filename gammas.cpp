#include <bits/stdc++.h>
using namespace std;


double means[2005];
gamma_distribution<double> distributions[2005];
int main(){
	freopen("gammas.out", "w", stdout);
	int q = 5000000;
	int n = 2000;
	for (int i = 1; i <= n; i++){
		gamma_distribution<double> distribution(i, 1);
		distributions[i] = distribution;
	}
	std::default_random_engine generator;
	for (int i = 0; i < q; i++){
		double x = 0;
		for (int j = 1; j <= n; j++){
			x = max(x, distributions[j](generator));
			means[j] += x;
		}
	}
	cout << fixed << setprecision(20);
	for (int j = 1; j <= n; j++){
		means[j] /= q;
		cout << j << ' ' << means[j] - j << endl;
	}
}
