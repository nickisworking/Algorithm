#include <iostream>

using namespace std;


int main() {
	int arr[5] = { 2,4,1,5,3 };

	for(int i = 0; i < 4; i++) {
		int min = 100000;
		int idx;
		for (int j = i; j < 5; j++) {
			if (min > arr[j]) {
				min = arr[j];
				idx = j;
			}
		}

		arr[idx] = arr[i];
		arr[i] = min;
	}

	for (int i = 0; i < 5; i++) {
		cout << arr[i]<< " ";
	}


}