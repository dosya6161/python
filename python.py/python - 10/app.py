# # Dasturlash asoslari

# # 10 - dars: TARMOQLANISH

avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hundai']
for avto in avtolar: # avtolar ichidagi har bir avto uchun
    if avto == 'bmw': # ... agar avto bmw ga teng bo'lsa
# if - agar
# == - tengmi 
        print(avto.upper()) # avto nomini hama harflarini katta qiladi
    else: # aks holda ...   
        print(avto.title()) # avto nomini faqat birinchi harfni katta qiladi
#
ism = 'Ali'

ism.lower() == 'ali'

ism = input('ismingiz nima?\n>>>') # Foydalanuvchi ismini 
if ism.lower() != 'ali': # != - teng emasmi !
    print(f"Uzr, {ism.title()} biz Alini kutayapmiz.")
else:
    print('Salom, Ali')
#
javob = float(input("12x6 nechiga teng?>>>"))
if javob!=72:
    print("javob xato!")
# 
yosh = int(input("Yoshingiz nechida?>>>"))
if yosh>=18: # yosh 18 dan katta yoki teng bo'lsa # >= -katta yoki teng
    print('Xush kelibsiz!')
else:
    print('Kirish mumkin emas!')
#
Login = input("Yangi login tanlang:")
if len(Login)<=5:
    print("Login 5 harfdan ko'proq bo'liahi shart!")
#
yil = int(input("Tug'ilgan yilingizni kiriting?>>>"))
if 2022-yil<18:
    print(f"Yoshingiz {2022-yil} ekan.")
    print("Kirish mumkin emas!")
else:
    print('Xush kelibsiz!')
#
yosh = int(input('Yoshingiz nechida?>>>'))
if yosh>65: print('Siz COVID-19 risk guruhida ekansiz')

x, y = 25, 50
print("x>y") if x>y else print("x>y")















