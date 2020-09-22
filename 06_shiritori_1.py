N, K, M = map(int, input().split())
player_num = [i for i in range(1, N + 1)]
word_list = []
for i in range(K):
    word_list.append(input())

flg = False
shiritori_word = []  # しりとりで使った言葉を格納するリスト
before_word = []  # しりとりが続いた場合、前の言葉を保持するリスト
end_char = ""
cnt = 0
for i in range(M):
    p = cnt % N
    word = input()
    if word not in word_list:  # ルール1
        cnt = p
        N -= 1
        del player_num[p]
        flg = False
        before_word = []
        continue
    if (i != 0) and (word in shiritori_word):  # ルール3
        cnt = p
        N -= 1
        del player_num[p]
        flg = False
        before_word = []
        continue
    if word[-1] == "z":  # ルール4
        cnt = p
        N -= 1
        del player_num[p]
        flg = False
        before_word = []
        continue

    before_word.append(word)
    start_char = word[0]
    if len(before_word) >= 2:
        end_char = before_word[-2][-1]
    if flg:
        if start_char != end_char:  # ルール2
            cnt = p
            N -= 1
            del player_num[p]
            flg = False
            before_word = []
            continue

    # 全てのルールに則った場合
    shiritori_word.append(word)
    flg = True
    cnt += 1

# 出力
print(len(player_num))
for num in player_num:
    if num != 0:
        print(num)
