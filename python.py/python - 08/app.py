# # DASTYRLASH ASSOSLARI !

# # 08-dars: LISTS !

# Tartiblash
cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla']
cars.sort() # sort() - metodi alfabit ketma ketligida tahlaydi ! 
print(cars)
list() # ro'yatga utqazadi #
# 
# # # Katta va kichik harf !
cars = ['Bmw', 'mercedes benz', 'volvo', 'gm', 'tesla']
cars.sort()
print(cars)
#
# # # Teskari tartib !
cars = ['Bmw', 'mercedes benz', 'volvo', 'general motors']
cars.sort(reverse=True) # reverse=True - matindi teskari tartibda tahlaydi !
print(cars)
#
# # # SORTED() - asil ro'yxatga teymagan xolda ro'yxatni elementlarini tartiblashimiz mumkin !
mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh' ]
print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
print(sorted(mehmonlar, reverse=True))
#
# # # Sonli ro'yxatlar !
ages = [12, 98, 34, 65, 34, 76, 11]
ages.sort()
print(ages)
print(sorted(ages, reverse=True))
#
# # # Ro'yxatni ortidan boshlab chiqarish !
fruits = ['pear', 'banana', 'apple', 'watermelon', 'Lemon']
fruits.reverse() # reverse() - yordamida ro'yxatni aylantirishimiz mumkin !
print(fruits)
#
# # # Ro'yxatmi uzunligi !
fruits = ['pear', 'banana', 'apple', 'watermelon', 'Lemon']
print("Elementlar soni", len(fruits)) # len - funksiyasi langes - uzunlik so'zidan olingan, ro'yxatlarni uzunligini chiqarish uchun foydalanamiz !  
# 
# # # Range - funksiyasi malum bir oraliqdegi sonlarni qaytaradi
sonlar = list(range(0,10))
print(sonlar)
#
# # # Range va qadam
juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam
toq_sonlar = list(range(1,20,2)) # 1 dan 20 gacha 2 qadam
print("Juft sonlar: ", juft_sonlar)
print("Toq sonlar: ", toq_sonlar)
#
# # MIN(), MAX(), SUM()
narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
arzon = min(narhlar)
qimmat = max(narhlar)
jami = sum(narhlar)
print("Eng arzon narh ", arzon, ". Eng qimmat ", qimmat, ". Jami: ", jami)
#
# # # Ro'yxatni kesish
cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla']
my_cars = cars[0:3] # indekisdan boshlab 3 ta element ajratadi
print(my_cars)
print(cars[2:5]) # 2-3-4-elementlarini ajratib olamiz  !
print(cars[:4]) # ro'yxat boshidan 4-gacha kesadi !
print(cars[2:]) # 2-elementdan boshlab ro'yxat oxirgacha chiqaradi !
# 
# # # Ro'yxatdan nusha olish !
sonlar = [1, 2, 3, 4, 5] # sonlar degan ro'yxat yaratamiz !
sonlar2 = sonlar # sonlar2 degan ro'yxatni sonlar ga tenglashtiramiz !
sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz 
sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz 
print("Bu sonlar ro'yxati:", sonlar)
print("Bu sonlar2 ro'yxati:", sonlar2)
#
# # # TUPLES - uzgarmas ro'yxat !
tomonlar = [20, 30, 55.2]
print(tomonlar)
#
toys = ("bus", "car", "bear", 'dino', 'snake', 'lizard')
print(toys[0])
print(toys[-1])
print(toys[2:5])
# 
toys = ("bus", "car", "bear", 'dino', 'snake', 'lizard')
toys[3] = 'dragon'
#
# # # TUPLES<->LIST
toys = ("bus", "car", "bear", 'dino', 'snake', 'lizard')
toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (LIST)
# # Ro'yxatga o'zgartirishlar kiritamiz !
toys.append('dragon')
toys.remove('bus')
toys[1] = 'mcqueen'
toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga o'tqazadi !
print(toys)












