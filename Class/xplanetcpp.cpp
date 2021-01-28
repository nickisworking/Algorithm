#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <time.h>
#include <set>
#include <map>
#include <unordered_map>
using namespace std;

char random_sent[201][1001];
char dnas[201][1001];

int main() {

	clock_t start, end;
	start = clock();

	double result;
	int max = 0;
	int N;

	FILE* fptr = fopen("xplanet.txt","r");
	fscanf(fptr,"%d\n", &N);
	
	//random 문자열 생성

	for (int i = 0; i < 200; i++) {
		for (int j = 0; j < 1000; j++) {
			fscanf(fptr, "%c", &dnas[i][j]);
		}
	}

	for (int i = 0; i < 200; i++) {
		for (int j = 0; j < 1000; j++) {
			cout << dnas[i][j];
		}
		cout << endl;
	}
	
	/*
	for (int i = 0; i < 200; i++) {
		for (int j = 0; j < 1000; j++) {
			random_sent[i][j] = 'A' + rand() % 26;
		}
		dnas[i] = random_sent[i];
	}
	*/

	
	//직접입력받기
	/*
	for (int i = 0; i < N; i++) {
		cin >> dnas[i];
	}
	*/


	//시간재기
	
	//알고리즘 - 매핑
	for (int i = 0; i < N; i++) {
		map<char*, int> dnaMap;
		int curSize = strlen(dnas[i]);
		for (int j = 0; j < curSize; j++) {
			char idx_sent[3];
			strncpy(idx_sent, dnas[i] + j, 3);
			
			if (dnaMap.insert(pair<char*, int>(idx_sent, 1)).second == false) {
				dnaMap.find(idx_sent)->second += 1;
				
				if (dnaMap.find(idx_sent)->second > max) {
					max = dnaMap.find(idx_sent)->second;
				}
				
			}		
		
		}
		
	}

	//시간
	end = clock();
	result = (double)end - start;

	//출력
	cout << result / CLOCKS_PER_SEC <<endl;
	cout << max;
	
}