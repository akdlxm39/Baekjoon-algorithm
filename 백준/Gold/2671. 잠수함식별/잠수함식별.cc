#include <bits/stdc++.h>
using namespace std;

#define MAX_STATE_NUM 10
#define MAX_STRING_SIZE 150

#define START_STATE 0
#define SINK_STATE (MAX_STATE_NUM-1)


string s;
int state = START_STATE;
int transition_table[MAX_STATE_NUM][2] = {
	{5,1},
	{2, SINK_STATE},
	{3, SINK_STATE},
	{3, 4},
	{5, 7},
	{SINK_STATE, 6},
	{5, 1},
	{8, 7},
	{3, 6},
	{SINK_STATE, SINK_STATE}
};

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	cin >> s;

	for (int i = 0; s[i] != '\0'; i++) {
		state = transition_table[state][s[i] - '0'];
	}

	if (state == 4 || state == 6 || state == 7) {
		puts("SUBMARINE");
	}
	else {
		puts("NOISE");
	}
}