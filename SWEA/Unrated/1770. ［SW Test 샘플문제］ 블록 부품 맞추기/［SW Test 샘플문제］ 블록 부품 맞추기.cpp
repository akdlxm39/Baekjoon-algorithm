#include <malloc.h>

#define MAX_N 30000

// 구조체 크기 최소화 (총 16바이트)
struct Block {
    unsigned long long C; // 4x4 형태를 4비트씩 16개로 압축한 64비트 정수 대표값
    int base_h;           // 원래 블록의 최소 높이
    int max_diff;         // 최대 높이차
};

// 16칸 배열을 64비트 정수로 압축
inline unsigned long long packArray(const int arr[16]) {
    unsigned long long res = 0;
    for (int i = 0; i < 16; ++i) {
        res = (res << 4) | (unsigned long long)arr[i];
    }
    return res;
}

// 4가지 회전 형태 중 가장 사전순으로 앞서는 64비트 정수 대표값 추출
unsigned long long getCanonical(const int src[16]) {
    unsigned long long best = 0xFFFFFFFFFFFFFFFFULL;
    int R[16];
    
    // 0도
    unsigned long long cand = packArray(src);
    if (cand < best) best = cand;
    
    // 90도
    for(int r = 0; r < 4; ++r)
        for(int c = 0; c < 4; ++c)
            R[r * 4 + c] = src[(3 - c) * 4 + r];
    cand = packArray(R);
    if (cand < best) best = cand;
    
    // 180도
    for(int r = 0; r < 4; ++r)
        for(int c = 0; c < 4; ++c)
            R[r * 4 + c] = src[(3 - r) * 4 + (3 - c)];
    cand = packArray(R);
    if (cand < best) best = cand;
    
    // 270도
    for(int r = 0; r < 4; ++r)
        for(int c = 0; c < 4; ++c)
            R[r * 4 + c] = src[c * 4 + (3 - r)];
    cand = packArray(R);
    if (cand < best) best = cand;
    
    return best;
}

inline void swapBlock(Block& a, Block& b) {
    Block t = a; a = b; b = t;
}

// 1순위: 형태(오름차순), 2순위: 기본 높이(내림차순)
void quickSort3Way(Block* arr, int left, int right) {
    if (left >= right) return;
    int lt = left, gt = right;
    unsigned long long pC = arr[left].C;
    int pBase = arr[left].base_h;
    
    int i = left + 1;
    while (i <= gt) {
        int cmp = 0;
        if (arr[i].C != pC) {
            cmp = arr[i].C < pC ? -1 : 1;
        } else if (arr[i].base_h != pBase) {
            cmp = arr[i].base_h > pBase ? -1 : 1; // 내림차순
        }
        
        if (cmp < 0) swapBlock(arr[lt++], arr[i++]);
        else if (cmp > 0) swapBlock(arr[i], arr[gt--]);
        else i++;
    }
    quickSort3Way(arr, left, lt - 1);
    quickSort3Way(arr, gt + 1, right);
}

// 이분 탐색: 압축된 64비트 정수(형태) 기반 Lower Bound
int findGroupStart(Block* arr, unsigned long long target_C, int N) {
    int left = 0, right = N - 1;
    int ans = -1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid].C < target_C) {
            left = mid + 1;
        } else if (arr[mid].C > target_C) {
            right = mid - 1;
        } else {
            ans = mid;
            right = mid - 1; 
        }
    }
    return ans;
}

int makeBlock(int module[][4][4]) {
    Block* blocks = (Block*)malloc(MAX_N * sizeof(Block));
    bool* processed = (bool*)malloc(MAX_N * sizeof(bool));
    
    for (int i = 0; i < MAX_N; ++i) {
        processed[i] = false;
        int min_h = 2000000000, max_h = -1;
        for (int r = 0; r < 4; ++r) {
            for (int c = 0; c < 4; ++c) {
                int h = module[i][r][c];
                if (h < min_h) min_h = h;
                if (h > max_h) max_h = h;
            }
        }
        blocks[i].base_h = min_h;
        blocks[i].max_diff = max_h - min_h;
        
        int norm1D[16];
        for (int r = 0; r < 4; ++r) {
            for (int c = 0; c < 4; ++c) {
                norm1D[r * 4 + c] = module[i][r][c] - min_h;
            }
        }
        blocks[i].C = getCanonical(norm1D);
    }
    
    quickSort3Way(blocks, 0, MAX_N - 1);
    
    int total_cost = 0;
    
    for (int i = 0; i < MAX_N; ++i) {
        if (processed[i]) continue;
        
        int g1_start = i, g1_end = i;
        unsigned long long current_C = blocks[g1_start].C;
        
        while (g1_end + 1 < MAX_N && blocks[g1_end + 1].C == current_C) {
            g1_end++;
        }
        
        // 64비트 정수를 16칸 배열로 디코딩
        int decoded[16];
        unsigned long long temp = current_C;
        for (int k = 15; k >= 0; --k) {
            decoded[k] = temp & 0xF;
            temp >>= 4;
        }
        
        // 보수 계산 및 좌우 반전 적용
        int Comp_flipped[16];
        int max_d = blocks[g1_start].max_diff;
        for(int r = 0; r < 4; ++r) {
            for(int c = 0; c < 4; ++c) {
                // 원본의 (r, 3-c) 위치의 보수값을 현재 (r, c)에 삽입
                Comp_flipped[r * 4 + c] = max_d - decoded[r * 4 + (3 - c)];
            }
        }
        
        unsigned long long TargetCan = getCanonical(Comp_flipped);
        
        if (current_C == TargetCan) {
            int p = g1_start;
            while (p + 1 <= g1_end) {
                total_cost += blocks[p].base_h + blocks[p+1].base_h + max_d;
                processed[p] = processed[p+1] = true;
                p += 2;
            }
        } else {
            int g2_start = findGroupStart(blocks, TargetCan, MAX_N);
            if (g2_start != -1) {
                int g2_end = g2_start;
                while (g2_end + 1 < MAX_N && blocks[g2_end + 1].C == TargetCan) {
                    g2_end++;
                }
                
                int p1 = g1_start, p2 = g2_start;
                while (p1 <= g1_end && p2 <= g2_end) {
                    total_cost += blocks[p1].base_h + blocks[p2].base_h + max_d;
                    processed[p1] = processed[p2] = true;
                    p1++; p2++;
                }
                for(int k = g2_start; k <= g2_end; ++k) processed[k] = true;
            }
        }
        
        for(int k = g1_start; k <= g1_end; ++k) processed[k] = true;
        i = g1_end;
    }
    
    free(blocks);
    free(processed);
    
    return total_cost;
}