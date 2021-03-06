import sys
sys.stdin = open('치킨배달_input.txt')

def solve():
    hap = 0
    for i in range(HN): # 현재 집에서 고른 치킨집과 최소인 거리 찾기
        dist_min = 20*20
        for j in range(CN): # 치킨집
            if not sel[j]: continue # 선택하지 않은 치킨집이면 스킵
            dist_min = min(dist_min, arr[j][i]) # 최소거리
        hap += dist_min
    return hap

def DFS(no, cnt):
    # 현재 치킨집을 고르거나 고르지 않는 경우 시도
    # M개 골랐을 때 고른 치킨거리의 최소의 합 비교
    global sol
    if cnt == M:
        hap = solve()
        if hap < sol: sol = hap
        return
    if no >= CN: return
    sel[no] = 1
    DFS(no + 1, cnt + 1)
    sel[no] = 0
    DFS(no + 1, cnt)


# main ------------------------------
N, M = map(int, input().split())
temp = [list(map(int, input().split())) for _ in range(N)]
chk = []
house = []
for i in range(N):
    for j in range(N):
        if temp[i][j] == 2:
            chk.append((i, j))
        elif temp[i][j] == 1:
            house.append((i, j))
CN = len(chk) # 치킨집개수
HN = len(house) # 집 개수
sel = [0]*HN # 고른 치킨집
arr = [[0]*HN for _ in range(CN)]  # 치킨집을 행, 집을 열로 놓음
for i in range(CN):
    for j in range(HN):
        dist = abs(chk[i][0] - house[j][0]) + abs(chk[i][1] - house[j][1]) # 치킨집 - 집 거리 계산
        arr[i][j] = dist
sol = 20*20
DFS(0, 0) # 0행(첫번째 치킨)부터 시작, 개수는 0개
print(sol)