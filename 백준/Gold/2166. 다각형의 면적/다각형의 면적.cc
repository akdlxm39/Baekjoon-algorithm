#include <bits/stdc++.h>
using namespace std;

struct point {
	double x, y;
};

struct line {
	point A, B;
	point v;
	double len;
	line(point A, point B) {
		this->A = A;
		this->B = B;
		make_v();
		len = sqrt(v.x * v.x + v.y * v.y);
	}
	void make_v() {
		v.x = A.x - B.x;
		v.y = A.y - B.y;
	}
};

double cross_product(const line& L1, const line& L2) {
	double res;
	res = L1.v.x * L2.v.y - L1.v.y * L2.v.x;
	return res;
}

int N;
point P[10001];
double area;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cout.precision(1);
	cout << fixed;

	cin >> N;
	for (int i = 1; i <= N; i++)
		cin >> P[i].x >> P[i].y;
	P[0].x = P[0].y = 0;

	for (int i = 1; i < N; i++) {
		line L1(P[0], P[i]), L2(P[0], P[i + 1]);
		area += cross_product(L1, L2) / 2;
	}
	area += cross_product(line(P[0], P[N]), line(P[0], P[1])) / 2;

	cout << abs(area) << '\n';

	return 0;
}