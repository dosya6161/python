# # # 07 - Dars List (Ro'yxatlar) !

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati.
narhlar  = [12000, 18000, 10900, 22000, 25000, 36000, -25, 63.2] # narxlar ro'yxati
sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat.
isimlar = [] # bo'sh ro'yxat.

print("Birinchi meva: ", mevalar[0])
print("Ikkinchi meva: ", mevalar[1])

print("Birinchi meva: ", mevalar[0].title())
print("Ikkinchi meva: ", mevalar[1].upper())
#
narhlar  = [12000, 18000, 10900, 22000]
print(narhlar[2] + narhlar[3])
#
car_models = ["tayota", 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswage']
print(car_models[-1]) # Listning eng oxirgi elementiga -1 bilan murojat qilish.

# # Elementni o'zgartirish !

narhlar  = [12000, 18000, 10900, 22000]
narhlar[0] = 13000 # 1-qiymatini 13000 ga o'zgartiramiz
narhlar[2] = 11000 # 3-qiymatini 11000 ga o'zgartiramiz
narhlar[3] = narhlar[3]+200 # 4-qiymatga 200 qo'shamiz
print(narhlar)


# .append() - ro'yxatga yangi sonlar va so'zlar qoshamiz.

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
mevalar.append("tarvuz") # mevalarga tarvuz qo'shamiz.
print(mevalar)
#
cars = [] # bo'sh ro'yxat yaratamiz 
cars.append('lacetti') # ro'yxatga lacetti mashinasini qo'shamiz
cars.append('Nexia 3') # ro'yxatga Nexia 3 mashinasini qo'shamiz
cars.append('Cobalt') # ro'yxatga Cobalt mashinasini qo'shamiz
print(cars)


# .insert 

cars = ['lacetti', 'Nexia 3', 'Cobalt']
cars.insert(0, 'Malibu') # 1 - o'ringa yangi qiymat qo'shamiz
print(cars)
cars.insert(2, 'Damas') # 3 - o'ringa yangi qiymat qo'shamiz
print(cars)
#
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
del mevalar[1] # 2-elementni (anjir) o'chirib tashemiz
print(mevalar)
#
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
mevalar.remove('shaftoli') # ro'yxatdan shaftolini o'chirdik
print(mevalar)
#
hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
hayvonlar.remove('mushuk') # ro'yxatda 2 ta mushuk bor, ulardan birinchisi o'chiriladi
print(hayvonlar)
#
bozorlik = ['yog\'', 'un', 'piyoz', 'banan', 'go\'sht']
mahsulot = bozorlik.pop(3) # ro'yxatdan banan ni sugurib olamiz
print("Men " + mahsulot + "sotib oldim")
print("Olinmagan mahsulotlar: ", bozorlik)
 
























