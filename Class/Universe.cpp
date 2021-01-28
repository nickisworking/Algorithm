#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <utility>
using namespace std;

pair<int, int> Universe[20][3001];
pair<int, int> B[3001];
int C[1000000];


void CountSort(pair<int, int> Universe[],int k, int n) {
	int i, j;

	for (i = 0; i <= k; i++) C[i] = 0;
	for (j = 1; j <= n; j++) C[Universe[j].first] = C[Universe[j].first] + 1;
	for (i = 1; i <= k; i++) C[i] = C[i] + C[i - 1];

	for (j = n; j >= 0; j--) {
		B[C[Universe[j].first]] = make_pair(Universe[j].first,Universe[j].second);
		C[Universe[j].first] -= 1;
	}

	for (i = 1; i <= n; i++) {
		Universe[i] = B[i];
	}
	//end CountSort

}

int main(int argc, const char* argv[]) {
	int n, m;
	int k[20] = { 0, };

	FILE* fptr;
	fptr = fopen("Universe.inp", "r");
	fscanf(fptr, "%d %d \n", &m, &n);

	//입력부분
	for (int i = 0; i < 2 * m; i++) { 
		for (int j = 1; j <= n; j++) {
			int input;
			fscanf(fptr, "%d", &input);
			if (input > k[i]) { k[i] = input; }
			Universe[i][j] = make_pair(input, j);
		}
	}

	fclose(fptr);

	int count = 0;
	int flag = 1;
	for (int i = 0; i < 2*m; i++) {
		CountSort(Universe[i], k[i], n);
	}
	
	

	for (int i = 0; i < 2 * m; i += 2) {
		for (int j = 1; j <= n; j++) {
			if (Universe[i][j].second != Universe[i + 1][j].second) {
				flag = 0; break;
			}
			if (j < n && Universe[i][j].first == Universe[i][j + 1].first && Universe[i + 1][j].second != Universe[i + 1][j + 1].second) {
				flag = 0; break;
			}


		}
		if (flag == 0) {
			flag = 1;
		}
		else {
			flag = 1; count++;
		}
	}

	cout << count;
	
	FILE* fp;
	fp = fopen("Universe.out", "w");
	fprintf(fp, "%d", count);
	fclose(fptr);

	




}