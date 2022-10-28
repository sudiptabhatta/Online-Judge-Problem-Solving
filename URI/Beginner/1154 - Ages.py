sum = 0
count = 0

while True:
    age = int(input())
    if age < 0:
        break
    else:
        count = count + 1
        sum = sum + age
        
print("%.2f"%(sum / count))