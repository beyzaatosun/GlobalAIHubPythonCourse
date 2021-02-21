# -*- coding: utf-8 -*-
"""
@author: BeyzaTosun
"""
import random

kontrol = False #asal sayı tutmak için oluşturduğumuz kontrol değişkeni
primeNumbers = []
for j in range(2,100): #asal sayılar bulmak için oluşturulan for döngüsü
   for i in range(2,j):
       if (j % i) == 0:
           break
   else:
       kontrol = True
   if kontrol == True:
       primeNumbers.append(j) #asal sayi ise primeNumbers'a ekler
       kontrol = False

matrix = [[0 for i in range(3)] for j in range(3)] #3x3'lük matris oluşturur

for i in range(3):
    for j in range(3):
        matrix[i][j] = primeNumbers[random.randint(0,(len(primeNumbers))-1)]
         #oluşturulan 3x3 'lük matrisi rastgele sayilar ile doldurur 
print(matrix)

