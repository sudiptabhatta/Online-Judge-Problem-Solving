values = input().split()

A, B, C = values 
# print(type(A))

maior = int((int(A) + int(B) + abs(int(A) - int(B)))/2)
maior1 = int((int(maior)+int(C)+abs(int(maior)-int(C)))/2)
print(f'{maior1} eh o maior')