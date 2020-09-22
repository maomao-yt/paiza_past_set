days, span = map(int, input().split())
visitors = [int(i) for i in input().split()]

# 初期処理
earliest_day = 0
num_of_candidate = 1
sum_visitor = sum(visitors[0:span])
largest_avg_visitor = sum_visitor / span

# 第2区間以降の処理
for i in range(1, days - span + 1):
    # sum関数で区間合計だすより前区間の値を利用して今区間の値を出す方が速い
    sum_visitor = sum_visitor - visitors[i - 1] + visitors[i + span - 1]
    avg_visitor = sum_visitor / span
    if avg_visitor == largest_avg_visitor:  # 今区間平均値が、現在の最大平均値と同じであれば
        num_of_candidate += 1  # 候補数をカウント
    elif avg_visitor > largest_avg_visitor:  # 今区間平均値が、現在の最大平均値より大きければ、
        earliest_day = i  # インデックス番号を更新
        largest_avg_visitor = avg_visitor  # 最大平均値の更新
        num_of_candidate = 1  # 候補数のリセット

print(num_of_candidate, earliest_day + 1)

