# # Dasturlash asoslari

# # 11 - dars: if-elif-else

son = 50
if son<0:
    print("Manfiy son")
else:
    print("Musbat son")
#
yosh = int(input('Yoshingiz nechida? '))    
if yosh<=4:
    print('Sizga kirish bepul.')
elif yosh<=12: # elif - aks holda, agar ! else, if operatorlarini yig'indisi 
    print('Sizga kirish 5000 so\'m')
elif yosh<18:
    print("Sizga kirish 8000 so'm")
else:
    print('Sizga kirish 10000 so\'m')
#
yosh = int(input('Yoshingiz nechida? '))    
if yosh<=4:
    narh = 0
elif yosh<=12:
    narh = 5000
elif yosh<18:
    narh = 8000
else:
    narh = 10000

print(f"Sizga kirish {narh} so'm!")
#
# or - yoki, operator
# and - va, operator
#
kun = input("Bugun nime kun?>>>")
if kun.lower()=='shanba' or kun.lower()=='yakshanba':
    print('Bugun dam olish kuni.')
else:
    print('Bugun ish kuni.')
#
kun = input("Bugun nima kun? ")
harorat = float(input("Havo harorati qanday? "))
if (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat>=30:
    print("Cho'milgani ketik!")
elif (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat<30:
    print("Uyda dam olamiz!")
#
# # # BOOLEAN - ma'lumotlar turi, mantiqiy ma'lumot turi bo'lib True - Folse
narh = 15000 # mijoz 15000 so'mga taom oldi.
choy = True # mijoz choy ham oldi
salat = False # mijoz salat olmadi

if choy and salat: # agar mijoz choy ham salat ham olgan bo'lsa
    narh = narh + 10000 # narhga 10000 so'm qo'shamiz
elif choy or salat: # agar choy yoki salat olgan bo'lsa
    narh = narh + 5000 # narhga 5000 so'm qo'shamiz 
    
print(f"Jami {narh} so'm") # yaluniy narhni chiqaramiz
#
narh = 15000 # mijoz 15000 so'mga ovqat oldi
choy = 1
salat = 0
non = 1 
kompot = 1 
assorti = 1
# Quyidagi har bir shart alohida tekshiriladi va bir biriga bog'liq emas
if choy: # agar choy olsa
    print("Mijooz choy oldi.")
    narh = narh + 3000
    
if salat: # agar salat olsa
    print("Mijoz salat oldi.")
    narh = narh + 5000
    
if non: # agar non olsa
    print("Mijoz non oldi.")
    narh = narh + 2000

if kompot : # agar kampot olsa
    print("Mijoz kampot oldi.")
    narh = narh + 5000

if assorti: # agar assorti olsa 
    print("Mijoz assorti oldi.")
    narh = narh + 15000
#
menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
ovqat = input('Nima ovqat yeysiz?>>>')
if ovqat.lower() not in menu:
    print('Afsuski bizda bunday ovqat yo\'q')
else:
    print('Buyurtma qabul qilindi.')
# not in - ma'lum bir elemetni ro'yxatda yo'qligini tekshirib koramiz
#
menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
buyurtmalar = ["osh", "somsa", "manti", "shashlik"]

for taom in buyurtmalar:
    if taom in menu:
        print(f"Menuda {taom} bor")
    else:
        print(f"Kechirasiz, menuda {taom} yo'q")
#
menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
buyurtmalar = ["osh", "somsa", "manti", "shashlik"]

if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda True qaytaradi 
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menuda {taom} bor")
        else:
            print(f"Kechirasiz, menuda {taom} yo'q")
else: #agar ro'yxat bo'sh bo'lsa
    print("Savatchangiz bo'sh!")














