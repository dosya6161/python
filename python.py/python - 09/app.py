# # Dasturlash asoslari

# # 09 - dars: FOR LOOP

mehmonlar = ['Ali', 'Vali', 'hasan', 'Husan', 'Olim']
for mehmon in mehmonlar: # for - so'zi uchun dib tarjima qilinadi
# for - malum br kodni qayta qayta takrorlash uchun takrorlanadi 
   print("Salom, ", mehmon)
   print("Xayr, ", mehmon)
#
mehmonlar = ['Ali', 'Vali', 'hasan', 'Husan', 'Olim']
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz    ")
    print("Hurmat bilan, palonchiyevlar oilasi\n")
#
mehmonlar = ['Ali', 'Vali', 'hasan', 'Husan', 'Olim']
for mehmon in mehmonlar:
    print(mehmon)

print(mehmonlar) # bu qator tsikl tashqarisida bo'lishi kerak edi
#
sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng")
#
sonlar = list(range(11)) # 1 dan 10 gacha sonlar ro'yxatini yaratamiz
sonlar_kvadrati = [] # bo'sh ro'yxat yaratamiz
for son in sonlar: # sonlardagi har bir son uchun 
    sonlar_kvadrati.append(son**2) # uning kv.ni hisoblab, sonlar_kvadrati
    
print(sonlar)
print(sonlar_kvadrati)
# 
dostlar = [] # bo'sh ro'yxat 
print("5 ta eng yaqin do'stingiz kim: ?")
for n in range(5):  # n bu yerda 0 dan 4 gacha qiymatlar oladi 
    dostlar.append(input(f"{n+1}-do'stingizni ismini kiriting: "))
print(dostlar)



















