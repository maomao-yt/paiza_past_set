H, W, N = map(int, input().split())
player = [0] * N  # プレイヤーの配点を管理するリストを作成

# トランプの配置を格納
field = []
for i in range(H):
    sub_field = []
    cards = input().split()
    for card in cards:
        sub_field.append(card)
    field.append(sub_field)

L = int(input())  # 試行回数

cnt = 0
for i in range(L):
    p = cnt % N  # プレイヤーの順番を管理
    y1, x1, y2, x2 = map(int, input().split())
    if field[y1-1][x1-1] == field[y2-1][x2-1]:
        player[p] += 2
    else:
        cnt += 1

# 出力
for ans in player:
    print(ans)
