#include <iostream>
using namespace std;



void MaxHeapify(int* arr, int i, int n);
void BuildMaxHeap(int* arr,int n);
void HeapSort(int* arr,int n);


int main() {
	int a[51];

	for (int i = 1; i < 51; i++) {
		a[i] = 51 - i;
	}

	cout << "Before sort : " << endl;

	for (int i = 1; i < 51; i++) {
		cout << a[i] << " ";
	}

	BuildMaxHeap(a, 50);
	HeapSort(a, 50);
	
	cout << endl;

	cout << "Before sort : " << endl;

	for (int i = 1; i < 51; i++) {
		cout << a[i] << " ";
	}


}

void MaxHeapify(int* arr, int i, int n) {
	int left_child = i * 2;
	int right_child = 2 * i + 1;
	int max = 0;

	if (left_child <= n && arr[i] < arr[left_child]) { max = left_child; }
	else { max = i; }

	if (right_child <= n && arr[right_child] > arr[max]) { max = right_child; }

	if (max != i) {
		int tmp = arr[i];
		arr[i] = arr[max];
		arr[max] = tmp;
		MaxHeapify(arr, max, n);
	}
}


void BuildMaxHeap(int* arr, int n) {

	for (int i = n / 2; i >= 1; i--) {
		MaxHeapify(arr, i, n);
	}

}


void HeapSort(int* arr,int n) {

	for (int i = n; i >= 2; i--) {
		int tmp = arr[i];
		arr[i] = arr[1];
		arr[1] = tmp;

		MaxHeapify(arr, 1, i-1);
		
	}
	
}
