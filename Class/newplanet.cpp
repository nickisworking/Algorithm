#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <time.h>
#include <map>
using namespace std;

char dnas[201][1001];

int hashCode(char* s) {
	int i;
	int r = 0;

	for (i = 0; i < 4; i++) {
		r += (r << 4) + s[i];
	}

	return r;
}

int main() {

	clock_t start, end;
	start = clock();

	double result;
	int max = 0;
	int N;

	FILE* fptr = fopen("xplanet.inp", "r");

	fscanf(fptr, "%d\n", &N);

	for (int i = 0; i < N; i++) {
		
		fscanf(fptr, "%s", &dnas[i]);
		
	}

	

	fclose(fptr);


	//알고리즘 - 매핑

	for (int i = 0; i < N; i++) {
		
		map<int, int> dnaMap;
		int curSize = strlen(dnas[i]) - 2;

		for (int j = 0; j < curSize; j++) {
			char idx_sent[4];

			strncpy(idx_sent, dnas[i] + j, 3);
			idx_sent[3] = '\0';
			int idx = hashCode(idx_sent);
			
			
			pair<map<int, int>::iterator, bool > pr;

			pr = dnaMap.insert(pair<int, int>(idx, 1));

			if(pr.second == false) {
				dnaMap[idx] += 1;
				if (dnaMap[idx] > max) {
					max = dnaMap[idx];
				}

			}

			//cout << "key : " << idx_sent << " value : " << dnaMap[idx] << endl;
		}
		map<int, int>::iterator j;
		cout << i << "번째 순회 : " << endl;
		for (j = dnaMap.begin(); j != dnaMap.end(); j++) {
			cout << j->first << " : " << j->second << endl;
		}

		//cout << "one iteration ends " << endl;
	}
	end = clock();

	result = (double)(end - start)/CLOCKS_PER_SEC;
	cout << result << endl;
	cout << max;
}