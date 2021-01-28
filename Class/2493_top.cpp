#include <iostream>
#include <stack>
#include <vector>
#include <utility>

using namespace std;

int main() {
	int N,i;
	cin >> N;
	stack <pair<int,int>> top;
	vector <int> result;

	
	for (i = 1; i <= N; i++) {
		int h;
		cin >> h;	
		pair <int, int> tmp = make_pair(h, i);

		if (top.empty()) { top.push(tmp); result.push_back(0);}
		else {
			
			while ((top.top().first < tmp.first)) {
				top.pop();
				if (top.empty()) { break; }
			}

			if (top.empty()) { top.push(tmp); result.push_back(0); }
			else{
			result.push_back(top.top().second);
			top.push(tmp);
			}
		}
	}

	for (int j = 0; j < result.size(); j++) {
		cout << result[j] << " ";
	}







	





}