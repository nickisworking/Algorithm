#include <iostream>
#define INF 111111;

using namespace std;


int map[501] = { 0, };
int weight[501][501] = { 0, };



int main() {
	int N, M;
	cin >> N >> M;

	for (int i = 2; i <= N; i++) {
		map[i] = INF;
	}
	
	map[1] = 0;


	for (int j = 1; j <= M; j++) {
	int start, destination, cost;
	cin >> start >> destination >> cost;
	weight[start][destination] = cost;
	}


	for (int i = 1; i <= N; i++) {	
		for (int j = 1; j <= N; j++) {
			if (weight[i][j] == 0) {
				continue;
			}
			else {
				if (map[j] >= map[i] + weight[i][j]) {
					map[j] = map[i]+weight[i][j];
				}
			}

		}
	}

	for (int i = 2; i <= N; i++) {
		cout << map[i] << endl;
	}



}