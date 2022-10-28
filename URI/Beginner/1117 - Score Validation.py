sum = 0
count = 0

while True: 
    if count == 2:
        break
    score = float(input())
    if score >= 0 and score <= 10:
        count = count + 1
        sum = sum + score
    else:
        print("nota invalida")

avg = sum / 2.00
print("media = %0.2f"%avg)
            
          