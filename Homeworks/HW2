# -*- coding: utf-8 -*-
"""
@author: BeyzaTosun
"""


info = {} 
studentsName = []
studentsGrades = []

for i in range(5):#5 öğrencinin bilgilerini almak için for döngüsü oluşturuldu
    studentsName.append(input("Öğrencinin adını giriniz:"))
    studentsName.append(input("Öğrencinin soyadını giriniz:"))
    studentsGrades.append(int(input("Öğrencinin vize notunu giriniz:")))
    studentsGrades.append(int(input("Öğrencinin ödev notunu giriniz:")))
    studentsGrades.append(int(input("Öğrencinin final notunu giriniz:")))
    info[studentsName[0] + " " + studentsName[1]] = studentsGrades.copy()
    studentsName.clear()
    studentsGrades.clear()

ortalama = 0
ortalamalar = {}
for i in info.items():#öğrencilerin ortalamalarının alındığı için for döngüsü 
    ortalama = sum(i[1])/len(i[1])
    ortalamalar[i[0]] = ortalama

ortalamalarSirali = sorted(ortalamalar.items(), key=lambda x: x[1], reverse=True)
#öğrencilerin ortalaması azalan sırada sıralandı

enIyiOgrenci = ' '
maxNot = 0
print("\n")
for i in ortalamalarSirali:#öğrencilerin ortalaması yazılması için for döngüsü
    print(str(i[0]) + " ortalamanız : " + str(i[1]))
    if i[1] > maxNot:
        maxNot = i[1]
        enIyiOgrenci = i[0]
#en yüksek notu alan öğrenci ekrana yazıldı
print(enIyiOgrenci + " Tebrikler!!")
