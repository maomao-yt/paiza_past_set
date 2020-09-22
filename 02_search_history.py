N = int(input())

history = []
for i in range(N):
    word = input()
    if word not in history:  # 検索ワードを先頭に追加する
        history.insert(0, word)
    else:  # 検索ワードを一旦削除し、先頭に追加
        index = history.index(word)
        del history[index]
        history.insert(0, word)

for word in history:
    print(word)
