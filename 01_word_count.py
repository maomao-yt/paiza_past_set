words =[i for i in input().split()]

# 元の順番を保持した重複排除
no_duplicate_words =list(sorted(set(words),key =words.index))

for word in no_duplicate_words:
    cnt = words.count(word)
    print(word, cnt)