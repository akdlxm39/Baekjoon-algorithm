#define MAX_NODES 480005
#define MAX_LEAVES 30005

// 트라이 메모리 풀
int children[MAX_NODES][3];
int leaf_id[MAX_NODES];

// 단말 노드 전용 데이터 풀
int counts[MAX_LEAVES][7];
int leaf_shapes[MAX_LEAVES][16];
int max_diffs[MAX_LEAVES];

int node_cnt;
int unique_cnt;

// 사전순으로 가장 앞서는 16칸 형태 배열 추출
void getCanonicalArray(const int src[16], int out[16]) {
    int best[16];
    for (int i = 0; i < 16; ++i) best[i] = src[i];

    int R[16];
    // 90도
    for (int r = 0; r < 4; ++r) 
        for (int c = 0; c < 4; ++c) R[r * 4 + c] = src[(3 - c) * 4 + r];
    bool smaller = false;
    for (int i = 0; i < 16; ++i) {
        if (R[i] != best[i]) { smaller = R[i] < best[i]; break; }
    }
    if (smaller) for (int i = 0; i < 16; ++i) best[i] = R[i];

    // 180도
    for (int r = 0; r < 4; ++r) 
        for (int c = 0; c < 4; ++c) R[r * 4 + c] = src[(3 - r) * 4 + (3 - c)];
    smaller = false;
    for (int i = 0; i < 16; ++i) {
        if (R[i] != best[i]) { smaller = R[i] < best[i]; break; }
    }
    if (smaller) for (int i = 0; i < 16; ++i) best[i] = R[i];

    // 270도
    for (int r = 0; r < 4; ++r) 
        for (int c = 0; c < 4; ++c) R[r * 4 + c] = src[c * 4 + (3 - r)];
    smaller = false;
    for (int i = 0; i < 16; ++i) {
        if (R[i] != best[i]) { smaller = R[i] < best[i]; break; }
    }
    if (smaller) for (int i = 0; i < 16; ++i) best[i] = R[i];

    for (int i = 0; i < 16; ++i) out[i] = best[i];
}

int makeBlock(int module[][4][4]) {
    // 1. 메모리 풀 초기화 (매 TC마다 첫 루트 노드만 초기화)
    children[0][0] = children[0][1] = children[0][2] = 0;
    leaf_id[0] = -1;
    node_cnt = 1;
    unique_cnt = 0;
    
    // 2. 블록 전처리 및 트라이 삽입
    for (int i = 0; i < 30000; ++i) {
        int min_h = 7, max_h = -1;
        for (int r = 0; r < 4; ++r) {
            for (int c = 0; c < 4; ++c) {
                int h = module[i][r][c];
                if (h < min_h) min_h = h;
                if (h > max_h) max_h = h;
            }
        }
        
        int diff = max_h - min_h;
        int norm1D[16];
        for (int r = 0; r < 4; ++r) {
            for (int c = 0; c < 4; ++c) {
                norm1D[r * 4 + c] = module[i][r][c] - min_h;
            }
        }
        
        int can[16];
        getCanonicalArray(norm1D, can);
        
        // 트라이 삽입
        int u = 0;
        for (int k = 0; k < 16; ++k) {
            int val = can[k];
            if (!children[u][val]) {
                children[u][val] = node_cnt;
                children[node_cnt][0] = children[node_cnt][1] = children[node_cnt][2] = 0;
                leaf_id[node_cnt] = -1;
                node_cnt++;
            }
            u = children[u][val];
        }
        
        // 새 단말 노드인 경우 데이터 풀 등록
        if (leaf_id[u] == -1) {
            leaf_id[u] = unique_cnt;
            for (int k = 0; k < 16; ++k) leaf_shapes[unique_cnt][k] = can[k];
            for (int k = 0; k < 7; ++k) counts[unique_cnt][k] = 0;
            max_diffs[unique_cnt] = diff;
            unique_cnt++;
        }
        
        counts[leaf_id[u]][min_h]++;
    }
    
    int total_cost = 0;
    
    // 3. 고유 형태(unique_cnt)별 짝 찾기 (Counting Sort 응용)
    for (int l = 0; l < unique_cnt; ++l) {
        int comp[16];
        int md = max_diffs[l];
        
        // 보수 및 좌우 반전 형태 계산
        for (int r = 0; r < 4; ++r) {
            for (int c = 0; c < 4; ++c) {
                comp[r * 4 + c] = md - leaf_shapes[l][r * 4 + (3 - c)];
            }
        }
        
        int target_can[16];
        getCanonicalArray(comp, target_can);
        
        // 트라이 탐색
        int u = 0;
        bool found = true;
        for (int k = 0; k < 16; ++k) {
            int val = target_can[k];
            if (!children[u][val]) { found = false; break; }
            u = children[u][val];
        }
        
        if (found && leaf_id[u] != -1) {
            int target_l = leaf_id[u];
            
            if (l == target_l) {
                // 자기 자신이 보수인 형태: 내부에서 자체 매칭
                int p = 6;
                while (p >= 1) {
                    if (counts[l][p] >= 2) {
                        counts[l][p] -= 2;
                        total_cost += (p + p + md);
                    } else if (counts[l][p] == 1) {
                        int next_p = p - 1;
                        while (next_p >= 1 && counts[l][next_p] == 0) next_p--;
                        if (next_p >= 1) {
                            counts[l][p]--;
                            counts[l][next_p]--;
                            total_cost += (p + next_p + md);
                        } else {
                            break;
                        }
                    } else {
                        p--;
                    }
                }
            } else if (l < target_l) {
                // 서로 다른 두 형태 매칭 (중복 연산 방지를 위해 l < target_l 인 경우만 처리)
                int p1 = 6, p2 = 6;
                while (p1 >= 1 && p2 >= 1) {
                    if (counts[l][p1] == 0) { p1--; continue; }
                    if (counts[target_l][p2] == 0) { p2--; continue; }
                    
                    counts[l][p1]--;
                    counts[target_l][p2]--;
                    total_cost += (p1 + p2 + md);
                }
            }
        }
    }
    
    return total_cost;
}