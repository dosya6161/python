# # 15-dars: Lug'at bilan ishlash

# # .items() - metodi elementlar 
talaba_0 = {
     'ism':'alijon',
     'familiya':'shamshiyev',
     'yosh':22,
     'fakultet':'matematika',
     'kurs':4
     }

print(talaba_0.items())
for key, value in talaba_0.items():
     print(f"Kalit: {key}")
     print(f"Qiymat: {value} \n")
#
telefonlar = {
     'ali':'iphone x',
     'vali':'galaxy s9',
     'olim':'mi 10 pro',
     'orif':'nokia 3310'
     }

for k, q in telefonlar.items():
     print(f"{k.title()}ning telefoni {q}")
#
# # .keys() - metodi kalit 
mahsulotlar = {
     'olma':10000,
     'anor':20000,
     'uzum':40000,
     'anjir':25000,
     'shaftoli':30000
     }

print(mahsulotlar.keys())

print('Do\'kondagi mahsulotlar:')
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())

print('Do\'kondagi mahsulotlar:')
for mahsulot in mahsulotlar:
     print(mahsulot.title())

bozorlik = ['anor','uzum','non','baliq']
for mahsulot in mahsulotlar:
     if mahsulot in bozorlik:
         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

for buyum in bozorlik:
     if buyum not in mahsulotlar:
        print(f"Iltimos, do'koningizga {buyum} ham olib keling")
        
# # LUG'AT ELEMENTLARINI TARTIB BILAN CHIQARISH
print("Do'konimizdagi mahsulotlar:")    
for mahsulot in sorted(mahsulotlar): # sorted() kalit so'z buyicha taxleydi
     print(mahsulot.title())
    
# # .values() - qiymat uzini chiqarad
print(telefonlar.values())

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in telefonlar.values():
     print(tel)


# # set - takrorlanekonlarni olib taweydida takrorlamekonlani qoldirad

telefonlar = {
     'ali':'iphone x',
     'vali':'galaxy s9',
     'olim':'mi 10 pro',
     'orif':'nokia 3310',
     'hamida':'galaxy s9',
     'maryam':'huawei p30',
     'tohir':'iphone x',
     'umar':'iphone x'    
     }

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in telefonlar.values():
     print(tel)
    
# # set - malu'mot turi
print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in set(telefonlar.values()):
     print(tel)

toys = {"ball","car","lamp","ball"} 
