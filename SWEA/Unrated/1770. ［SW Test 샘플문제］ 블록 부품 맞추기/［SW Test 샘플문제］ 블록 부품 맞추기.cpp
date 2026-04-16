#include <malloc.h>

#define MAX_N 30000
#define HASH_SIZE 262144
#define HASH_MASK 262143

#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define MIN4(a, b, c, d) MIN(MIN(a, b), MIN(c, d))

static unsigned int ht_C[HASH_SIZE];
static unsigned char ht_max_diff[HASH_SIZE];
static unsigned short ht_counts[HASH_SIZE][8];
static unsigned char state_tc[HASH_SIZE];
static unsigned int unique_keys[MAX_N];
static int current_tc = 0;

inline unsigned int hash32(unsigned int x)
{
    x ^= x >> 16;
    x *= 0x85ebca6b;
    x ^= x >> 13;
    x *= 0xc2b2ae35;
    x ^= x >> 16;
    return x;
}

// 추출 및 비트 시프트를 위한 매크로 (코드 가독성 극대화)
#define V(r, c) (module_i[r][c] - min_h)

inline unsigned int getCanonicalInline(const int module_i[4][4], int min_h)
{
    unsigned int b0 = (V(0, 0) << 30) | (V(0, 1) << 28) | (V(0, 2) << 26) | (V(0, 3) << 24) | (V(1, 0) << 22) |
                      (V(1, 1) << 20) | (V(1, 2) << 18) | (V(1, 3) << 16) | (V(2, 0) << 14) | (V(2, 1) << 12) |
                      (V(2, 2) << 10) | (V(2, 3) << 8) | (V(3, 0) << 6) | (V(3, 1) << 4) | (V(3, 2) << 2) | V(3, 3);

    unsigned int b1 = (V(3, 0) << 30) | (V(2, 0) << 28) | (V(1, 0) << 26) | (V(0, 0) << 24) | (V(3, 1) << 22) |
                      (V(2, 1) << 20) | (V(1, 1) << 18) | (V(0, 1) << 16) | (V(3, 2) << 14) | (V(2, 2) << 12) |
                      (V(1, 2) << 10) | (V(0, 2) << 8) | (V(3, 3) << 6) | (V(2, 3) << 4) | (V(1, 3) << 2) | V(0, 3);

    unsigned int b2 = (V(3, 3) << 30) | (V(3, 2) << 28) | (V(3, 1) << 26) | (V(3, 0) << 24) | (V(2, 3) << 22) |
                      (V(2, 2) << 20) | (V(2, 1) << 18) | (V(2, 0) << 16) | (V(1, 3) << 14) | (V(1, 2) << 12) |
                      (V(1, 1) << 10) | (V(1, 0) << 8) | (V(0, 3) << 6) | (V(0, 2) << 4) | (V(0, 1) << 2) | V(0, 0);

    unsigned int b3 = (V(0, 3) << 30) | (V(1, 3) << 28) | (V(2, 3) << 26) | (V(3, 3) << 24) | (V(0, 2) << 22) |
                      (V(1, 2) << 20) | (V(2, 2) << 18) | (V(3, 2) << 16) | (V(0, 1) << 14) | (V(1, 1) << 12) |
                      (V(2, 1) << 10) | (V(3, 1) << 8) | (V(0, 0) << 6) | (V(1, 0) << 4) | (V(2, 0) << 2) | V(3, 0);

    unsigned int best = MIN4(b0, b1, b2, b3);
    return best;
}

// 반복 갱신용 매크로
#define CHK_H(r, c)                                                                                                    \
    h = module[i][r][c];                                                                                               \
    if (h < min_h)                                                                                                     \
        min_h = h;                                                                                                     \
    if (h > max_h)                                                                                                     \
        max_h = h;

int makeBlock(int module[][4][4])
{
    current_tc += 2;

    int unique_cnt = 0;

    for (int i = 0; i < MAX_N; ++i)
    {
        int min_h = 7, max_h = -1, h;

        // 매크로를 이용한 직관적인 루프 언롤링
        CHK_H(0, 0) CHK_H(0, 1) CHK_H(0, 2) CHK_H(0, 3);
        CHK_H(1, 0) CHK_H(1, 1) CHK_H(1, 2) CHK_H(1, 3);
        CHK_H(2, 0) CHK_H(2, 1) CHK_H(2, 2) CHK_H(2, 3);
        CHK_H(3, 0) CHK_H(3, 1) CHK_H(3, 2) CHK_H(3, 3);

        unsigned int can = getCanonicalInline(module[i], min_h);
        unsigned int idx = hash32(can) & HASH_MASK;

        while ((state_tc[idx] & 0xFE) == current_tc && ht_C[idx] != can)
        {
            idx = (idx + 1) & HASH_MASK;
        }

        if ((state_tc[idx] & 0xFE) != current_tc)
        {
            state_tc[idx] = current_tc;
            ht_C[idx] = can;
            ht_max_diff[idx] = max_h - min_h;
            ht_counts[idx][1] = ht_counts[idx][2] = ht_counts[idx][3] = 0;
            ht_counts[idx][4] = ht_counts[idx][5] = ht_counts[idx][6] = 0;
            unique_keys[unique_cnt++] = can;
        }
        ht_counts[idx][min_h]++;
    }

    int total_cost = 0;

    for (int u = 0; u < unique_cnt; ++u)
    {
        unsigned int current_C = unique_keys[u];
        unsigned int idx1 = hash32(current_C) & HASH_MASK;
        while ((state_tc[idx1] & 0xFE) == current_tc && ht_C[idx1] != current_C)
        {
            idx1 = (idx1 + 1) & HASH_MASK;
        }

        if (state_tc[idx1] == current_tc + 1)
            continue;

        int max_d = ht_max_diff[idx1];
        int comp_arr[4][4];

        for (int k = 15; k >= 0; --k)
        {
            int r = k / 4, c = k % 4;
            comp_arr[r][3 - c] = max_d - (current_C & 0x3);
            current_C >>= 2;
        }

        unsigned int target_can = getCanonicalInline(comp_arr, 0);

        if (ht_C[idx1] == target_can)
        {
            int max_val = 0, left = 0;
            for (int p = 6; p >= 1; --p)
            {
                while (ht_counts[idx1][p] > 0)
                {
                    if (left == 0)
                    {
                        max_val = p;
                        left = 1;
                    }
                    else
                    {
                        total_cost += (max_val + p + max_d);
                        left = 0;
                    }
                    ht_counts[idx1][p]--;
                }
            }
            state_tc[idx1] = current_tc + 1;
        }
        else
        {
            unsigned int idx2 = hash32(target_can) & HASH_MASK;
            while ((state_tc[idx2] & 0xFE) == current_tc && ht_C[idx2] != target_can)
            {
                idx2 = (idx2 + 1) & HASH_MASK;
            }

            if ((state_tc[idx2] & 0xFE) == current_tc)
            {
                int p1 = 6, p2 = 6;
                while (p1 >= 1 && p2 >= 1)
                {
                    if (ht_counts[idx1][p1] == 0)
                    {
                        p1--;
                        continue;
                    }
                    if (ht_counts[idx2][p2] == 0)
                    {
                        p2--;
                        continue;
                    }

                    int pairs = MIN(ht_counts[idx1][p1], ht_counts[idx2][p2]);

                    ht_counts[idx1][p1] -= pairs;
                    ht_counts[idx2][p2] -= pairs;
                    total_cost += pairs * (p1 + p2 + max_d);
                }
                state_tc[idx2] = current_tc + 1;
            }
            state_tc[idx1] = current_tc + 1;
        }
    }

    return total_cost;
}