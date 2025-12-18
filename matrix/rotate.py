import sys
input = sys.stdin.readline

def main():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    for j in range(n):
        top, bottom = 0, n - 1
        while top < bottom:
            arr[top][j], arr[bottom][j] = arr[bottom][j], arr[top][j]
            top += 1
            bottom -= 1

    out = []
    for row in arr:
        out.append(" ".join(map(str, row)))
    print("\n".join(out))

if __name__ == "__main__":
    main()
