#include <bits/stdc++.h>
using namespace std;
#define MAX 402


struct edge {
	int from, to, capacity, flow;
	edge* reverse_edge;

	edge(int u, int v, int c) {
		from = u;
		to = v;
		capacity = c;
		flow = 0;
		reverse_edge = NULL;
	}

	int residual() {
		return capacity - flow;
	}

	void add_flow(int new_flow) {
		flow += new_flow;
		reverse_edge->flow -= new_flow;
	}
};

struct flow {
	int V, E;
	int source, sink;
	vector<edge*> adj[MAX];
	int total_flow;

	void add_edge(int u, int v, int c, bool directed = true) {
		edge* e1 = new edge(u, v, c);
		edge* e2 = new edge(v, u, (directed) ? 0 : c);
		e1->reverse_edge = e2;
		e2->reverse_edge = e1;
		adj[u].push_back(e1);
		adj[v].push_back(e2);
	}

	bool find_augmenting_path_bfs(int* trace, edge** back_edge) {
		for (int i = 0; i < MAX; i++) {
			trace[i] = -1;
			back_edge[i] = 0;
		}
		queue<int> q;
		q.push(source);
		while (!q.empty() && trace[sink] == -1) {
			int now = q.front(); q.pop();
			for (edge* e : adj[now]) {
				int next = e->to;
				if (trace[next] == -1 && e->residual() > 0) {
					trace[next] = now;
					back_edge[next] = e;
					q.push(next);
				}
			}
		}
		if (trace[sink] == -1) return false;
		return true;
	}

	int find_max_flow() {//flow는 어차피 1
		int trace[MAX];
		edge* back_edge[MAX] = { 0 };
		while (find_augmenting_path_bfs(trace, back_edge)) {
			int new_flow = 1;
			/*for (int i = sink; i != source; i = trace[i]) {
				new_flow = min(new_flow, back_edge[i]->residual());
			}*/
			for (int i = sink; i != source; i = trace[i]) {
				back_edge[i]->add_flow(new_flow);
			}
			total_flow += new_flow;
		}
		return total_flow;
	}


} G;

void input() {
	int N, M, S, w;

	cin >> N >> M;
	for (int i = 1; i <= N; i++) {
		cin >> S;
		while (S--) {
			cin >> w;
			G.add_edge(i, w + N, 1);
		}
	}
	G.source = 0;
	G.sink = N + M + 1;
	for (int i = 1; i <= N; i++)
		G.add_edge(0, i, 1);
	for (int i = N + 1; i <= N + M; i++)
		G.add_edge(i, N + M + 1, 1);
}


int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	input();
	G.find_max_flow();
	cout << G.total_flow << '\n';

	return 0;
}