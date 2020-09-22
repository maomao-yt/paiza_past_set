def judge(num):
    # 前後賞用の数値計算
    up = str(int(win_num) + 1)
    down = str(int(win_num) - 1)

    if up == "200000":
        if num == down:
            return "adjacent"  # 前後賞
    elif down == "99999":
        if num == up:
            return "adjacent"  # 前後賞
    elif (num == up) or (num == down):
        return "adjacent"  # 前後賞

    if num == win_num:  # 1等
        return "first"
    if num[2:] == win_num[2:]:  # 2等
        return "second"
    if num[3:] == win_num[3:]:  # 3等
        return "third"

    return "blank"


win_num = input()
N = int(input())
for i in range(N):
    num = input()
    print(judge(num))
