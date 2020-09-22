# よりコードを短くした
days, span = map(int, input().split())
visitors = [int(i) for i in input().split()]

# 初期処理
sum_visitor = sum(visitors[0:span])
avg_visitor = sum_visitor / span

span_list = [avg_visitor]
# 第2区間以降の処理
for i in range(1, days - span + 1):
    # sum関数で区間合計だすより前区間の値を利用して今区間の値を出す方が速い
    sum_visitor = sum_visitor - visitors[i - 1] + visitors[i + span - 1]
    avg_visitor = sum_visitor / span
    span_list.append(avg_visitor)

print(span_list.count(max(span_list)), span_list.index(max(span_list)) + 1)  # 候補日のカウント値、初期候補日を出力
