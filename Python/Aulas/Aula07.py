'''
for i in [0,1,2,3,4,5,6,7,8,9]:
    num = int(input("Diga um número:"))
    if num%2 == 0:
        pares += 1

for i range(10):
    print (i)
    i = 0
    print(i)

for i in range(1,10,2):#(ini, fim, passo)
        print(i)

for i in range(20,0,-2):
    print(i)
'''

a = 1
b = 1
for i in range(10):
    c = a+b
    a = b
    b = c
    print(c)