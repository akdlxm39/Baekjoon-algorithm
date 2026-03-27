// https://www.acmicpc.net/problem/7469 K번째 수 (바텀업 세그먼트 트리 최적화 버전)
#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

const int MAX = 1000000000;
const int MAX_N = 100000;

// 바텀업 트리를 위한 2N 크기의 벡터 배열
vector<int> tree[2 * MAX_N];
int n, m;

// 1. 바텀업 트리 초기화
void init() {
    // 리프 노드 제외한 내부 노드들을 역순으로 병합
    for (int i = n - 1; i > 0; --i) {
        merge(tree[i << 1].begin(), tree[i << 1].end(),
              tree[i << 1 | 1].begin(), tree[i << 1 | 1].end(),
              back_inserter(tree[i]));
    }
}

// 2. 바텀업 구간 쿼리: [l, r] 구간 내에서 val 이하인 수의 개수 반환
int count_less_equal(int l, int r, int val) {
    int res = 0;
    // 리프 노드 인덱스로 변환 (0-based)
    l += n;
    r += n;
    
    while (l <= r) {
        // l이 오른쪽 자식이면 병합 범위에 포함 후 l 전진
        if (l % 2 == 1) {
            res += int(upper_bound(tree[l].begin(), tree[l].end(), val) - tree[l].begin());
            l++;
        }
        // r이 왼쪽 자식이면 병합 범위에 포함 후 r 후진
        if (r % 2 == 0) {
            res += int(upper_bound(tree[r].begin(), tree[r].end(), val) - tree[r].begin());
            r--;
        }
        // 부모 노드로 이동
        l >>= 1;
        r >>= 1;
    }
    return res;
}

// 3. 파라메트릭 서치 로직 (이전과 동일)
int query(int i, int j, int k) {
    int left = -MAX, right = MAX;
    int ans = MAX;
    
    // 1-based 쿼리 입력을 0-based 내부 로직에 맞게 조정
    i--; j--; 
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (count_less_equal(i, j, mid) >= k) {
            ans = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return ans;
}

void solve() {
    cin >> n >> m;
    // 바텀업 트리는 리프 노드가 n번 인덱스부터 시작
    for (int i = 0; i < n; i++) {
        int val;
        cin >> val;
        tree[n + i].push_back(val);
    }
    
    init();
    
    while (m--) {
        int i, j, k;
        cin >> i >> j >> k;
        cout << query(i, j, k) << '\n';
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    solve();
    
    return 0;
}