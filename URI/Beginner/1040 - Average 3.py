scores = input().split()

N1, N2, N3, N4 = scores

average = (2 * float(N1) + 3 * float(N2) + 4 * float(N3) + 1 * float(N4)) / (2 + 3 + 4 + 1)

if average >= 7.0:
    print('Media: %.1f'%average)
    print('Aluno aprovado.')
elif average < 5.0:
    print('Media: %.1f'%average)
    print('Aluno reprovado.')
elif average >= 5.0 and average <= 6.9:
    exam_score = float(input())
    print('Media: %.1f'%average)
    print('Aluno em exame.')
    print(f'Nota do exame: {exam_score}')
    final_average = (exam_score + average) / 2
    if final_average >= 5.0:
        print('Aluno aprovado.')
        print(f'Media final: {final_average}')
    elif final_average <= 4.9:
        print('Aluno reprovado.')
        print(f'Media final: {final_average}')

