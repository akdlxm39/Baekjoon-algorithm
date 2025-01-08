#include <iostream>
#include <vector>
#include <string>
using namespace std;

int N, K;
string input;
vector<int> num;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> N >> K >> input;
	for (int i = 0; i < N; i++) {
		while (!num.empty() && K > 0 && num.back() < input[i] - '0') {
			num.pop_back();
			K--;
		}
		num.push_back(input[i] - '0');
	}
	if (K < 0) K = 0;
	for (int i = 0; i < num.size() - K; i++) cout << num[i];

	return 0;
}