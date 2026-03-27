// https://www.acmicpc.net/problem/7469 K번째 수 (N * logN 배열 최적화 버전)
#include <iostream>
#include <algorithm>

using namespace std;

const int MAX = 1000000000;
const int MAX_N = 100001;
// N=100000일 때 log2(N)은 약 16.6. 여유를 두어 18로 설정
const int MAX_DEPTH = 18; 

// vector 대신 N * logN 크기의 고정 2차원 배열 사용
int tree[MAX_DEPTH][MAX_N];
int arr[MAX_N];
int n, m;

// node 번호 대신 depth를 추적
void init(int depth, int left, int right) {
    if (left == right) {
        tree[depth][left] = arr[left];
        return;
    }
    
    int mid = left + (right - left) / 2;
    
    // 자식 노드(다음 깊이) 초기화
    init(depth + 1, left, mid);
    init(depth + 1, mid + 1, right);
    
    // 자식 깊이(depth + 1)에 정렬된 두 구간을 현재 깊이(depth)의 [left, right] 공간으로 병합
    merge(tree[depth + 1] + left, tree[depth + 1] + mid + 1,
          tree[depth + 1] + mid + 1, tree[depth + 1] + right + 1,
          tree[depth] + left);
}

int count_less_equal(int depth, int left, int right, int i, int j, int val) {
    if (right < i || j < left) return 0;
    
    if (i <= left && right <= j) {
        // vector의 begin(), end() 대신 배열의 포인터 연산 사용
        return int(upper_bound(tree[depth] + left, tree[depth] + right + 1, val) - (tree[depth] + left));
    }
    
    int mid = left + (right - left) / 2;
    return count_less_equal(depth + 1, left, mid, i, j, val) + 
           count_less_equal(depth + 1, mid + 1, right, i, j, val);
}

int query(int i, int j, int k) {
    int left = -MAX, right = MAX;
    int ans = MAX;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        // 탐색은 항상 루트(depth 0)에서 시작
        if (count_less_equal(0, 1, n, i, j, mid) >= k) {
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
    for (int i = 1; i <= n; i++) {
        cin >> arr[i];
    }
    
    // 루트 노드는 깊이 0에서 시작
    init(0, 1, n);
    
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