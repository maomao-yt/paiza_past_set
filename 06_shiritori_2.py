# よりコードを短くする
N, K, M = map(int, input().split())
player_num = [i for i in range(1, N + 1)]  # プレイヤーの番号リスト

word_list = []
for i in range(K):
    word_list.append(input())

flg = False
shiritori_word = []  # しりとりで使った言葉を格納するリスト
before_word = ""
turn = 0
for i in range(M):
    word = input()
    if word not in word_list:  # ルール1
        player_num.pop(turn)
        before_word = ""
    elif (before_word != "") and (word[0] != before_word[-1]):  # ルール2
        player_num.pop(turn)
        before_word = ""
    elif (i != 0) and (word in shiritori_word):  # ルール3
        player_num.pop(turn)
        before_word = ""
    elif word[-1] == "z":  # ルール4
        player_num.pop(turn)
        before_word = ""
    else:
        # 全てのルールに則った場合
        before_word = word
        shiritori_word.append(word)
        turn += 1
    # プレイヤーの最後まで順番が回ってきたら順番を最初に戻す
    if len(player_num) == turn:
        turn = 0

# 出力
print(len(player_num))
for num in player_num:
    if num != 0:
        print(num)
