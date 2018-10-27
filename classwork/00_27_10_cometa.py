A = int (input ('Введите год рождения \n'))
B = int (input ('Введите год смерти \n'))
C = int (input ('Кратность \n'))
k=0
while A<=B:
    A=A+1
    if A%C==0:
        k=k+1
print (k)
