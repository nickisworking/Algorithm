#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;


unsigned long long solve(unsigned long long k, unsigned long long result) {

	if (k == 0) { return result; }
	if (result % 2 == 1) {return solve(k - 1, result * 2); }

	else if(result%2 == 0 && (((result-1)/3)%2 == 1) && (((result - 1) / 3)>1) &&((result - 1)%3==0)){
		return	min(solve(k - 1, result * 2), solve(k - 1, (result - 1) / 3));
	}
	else if(result%2 == 0) { return solve(k - 1, result * 2); }


}


int main() {
	int k;
	long long ans;

	FILE* fptr = fopen("3n1.inp", "r");
	fscanf(fptr, "%d", &k);

	ans = solve(k, 1);
	
	FILE* fp = fopen("3n1.out", "w");

	fprintf(fp, "%llu %.0Lf", ans, pow(2,k));

	fclose(fp);
	fclose(fptr);

}