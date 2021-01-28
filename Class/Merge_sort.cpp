#include <iostream>
using namespace std;


int a[50];

void Merge_Sort(int* arr, int low, int high);
void Merge(int* arr, int low, int mid, int high);

int main() {
	
	for (int i = 0; i < 50; i++) {
		a[i] = 50 - i;
	}
	
	cout << "Before sort : " << endl;
	
	for (int i = 0; i < 50; i++) {
		cout << a[i] << " ";
	}

	cout << endl;

	Merge_Sort(a, 0, 49);

	cout << "After mergesort : " << endl;

	for (int i = 0; i < 50; i++) {
		cout << a[i] << " ";
	}

}

void Merge_Sort(int* arr, int low, int high) {

	int mid;
	if (low < high) {
		mid = (low + high) / 2;

		Merge_Sort(arr, low, mid);
		Merge_Sort(arr, mid + 1, high);
		Merge(arr, low, mid, high);
	}
}


void Merge(int* arr, int low, int mid, int high) {
	
	int i, k, j, h;
	int b[50];

	i = low; h = low; j = mid + 1; 

	while (h <= mid && j <= high) {
		if (arr[h] <= arr[j]) { b[i] = arr[h]; h++; }
		else { b[i] = arr[j]; j++; }
		i++;
	}

	if (h > mid) {
		for (k = j; k <= high; k++) {
			b[i] = a[k]; i++;
		}
	}
	else {
		for (k = h; k <= mid; k++) {
			b[i] = a[k]; i++;
		}
	}

	for (k = low; k <= high; k++) {
		a[k] = b[k];
	}



}
