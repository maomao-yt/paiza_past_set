days, span = map(int, input().split())
visitors = [int(i) for i in input().split()]

i = 0
span_list = []
for i in range(days-span+1):
    sum_visitor_avg = sum(visitors[i:i + span])/span
    span_list.append(sum_visitor_avg)

max_num = [i for i, x in enumerate(span_list) if x == max(span_list)] #複数の最大数のインデックス値を格納
print(len(max_num), max_num[0] + 1)
