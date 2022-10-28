duration_sec = int(input())

hours = duration_sec // 3600
minutes = duration_sec // 60
seconds = duration_sec - minutes * 60
minutes = minutes - hours*60

print(f'{hours}:{minutes}:{seconds}')