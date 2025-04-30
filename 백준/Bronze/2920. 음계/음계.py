import sys
input = sys.stdin.readline

def main():
    music = input().rstrip().replace(' ', '')
    if music == '12345678':
        print('ascending')
    elif music == '87654321':
        print('descending')
    else:
        print('mixed')

if __name__ == "__main__":
    main()