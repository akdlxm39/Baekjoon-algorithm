#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;


int N, K;
int t[100001];
priority_queue<pii,vector<pii>, greater<pii>> pq;

void dijkstra(int vertex) {
	pq.emplace(pii{ t[vertex], vertex });

	while (!pq.empty()) {
		int now = pq.top().second;
		int now_t = pq.top().first;
		pq.pop();
		if (t[now] < now_t) continue;
		for (pii next : { pii{now - 1, 1}, pii{ now + 1,1 }, pii{ now * 2, 0 }}) {
			if (next.first >= 0 && next.first <= 100000) {
				if (t[next.first] > now_t + next.second) {
					t[next.first] = now_t + next.second;
					pq.emplace(pii{ now_t + next.second, next.first });
				}
			}
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> N >> K;
	fill(t, t + 100001, INT_MAX);
	t[N] = 0;
	dijkstra(N);
	cout << t[K] << '\n';
}