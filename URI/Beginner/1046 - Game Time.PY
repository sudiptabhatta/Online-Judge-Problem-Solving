start_time, end_time = list(map(int, input().split()))

if start_time < end_time:
    time = end_time - start_time
else:
    time = end_time + 24 - start_time

print(f"O JOGO DUROU {time} HORA(S)")