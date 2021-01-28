#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdlib>

using namespace std;

long long product[200001];

int compare(const void* a, const void* b)    
{
	long long num1 = *(long long*)a;    
	long long num2 = *(long long*)b;    

	if (num1 < num2)    
		return 1;      

	if (num1 > num2)    
		return -1;       

	return 0;    
}



int main(int argc, const char* argv[]) {
	int N;
	long long dc = 0;
	
	FILE* fptr;
	fptr = fopen("shopping.inp", "r");
	fscanf(fptr, "%d\n", &N);

	for (int i = 0; i < N; i++) {
		fscanf(fptr, "%lld", &product[i]);
	}
	
	fclose(fptr);

	
	qsort(product, N,sizeof(long long),compare);
	
	for (int i = 0; i < N; i++) {
		if ((i+1) % 3 == 0) {
			dc += product[i];
		}
		else {
			continue;
		}
	}

	FILE* fp;
	fp = fopen("shopping.out", "w");
	fprintf(fp, "%lld", dc);
	fclose(fptr);
	
	return 0;
	
}