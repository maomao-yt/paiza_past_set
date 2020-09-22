def judge(ball):
    global ball_cnt,strike_cnt

    if ball == "ball":
        ball_cnt += 1
        if ball_cnt < 4:
            return "ball!"
        return "fourball!"
    else:
        strike_cnt += 1
        if strike_cnt < 3:
            return "strike!"
        return "out!"


N = int(input())

ball_cnt = 0  # ボールをカウント
strike_cnt = 0  # ストライクをカウント
for i in range(N):
    ball = input()
    print(judge(ball))
