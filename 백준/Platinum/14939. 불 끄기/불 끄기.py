import sys

input = sys.stdin.readline

def turn_off(light, prev_switch, min_click):
    click = 0
    next_switch = 0
    for cur_switch in light:
        click += prev_switch.bit_count()
        if click >= min_click:
            return 101
        cur_switch = cur_switch ^ next_switch
        next_switch = prev_switch
        prev_switch = cur_switch ^ prev_switch ^ ((prev_switch << 1) & 1023) ^ (prev_switch >> 1)
    return 101 if prev_switch else click


def main():
    light = []
    for _ in range(10):
        line = input().rstrip()
        tmp = 0
        for c in line:
            tmp <<= 1
            if c == 'O':
                tmp |= 1
        light.append(tmp)
    ans = 101
    for i in range(1024):
        ans = min(ans, turn_off(light, i, ans))
    print(ans if ans != 101 else -1)


if __name__ == "__main__":
    main()
