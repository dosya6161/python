# # 14 - dars: Dictionary (Lu'gat)

# # Key-value pair - Kalit so'z-qiymat juftligi !

car_0 = {'model':'ferrari','rang':'qizil'}
print(car_0['model'])
print(car_0['rang'])
#
en_uz = {'apple':'olma', 'apricot':'o\'rik', 'banana':"banan"}
print(en_uz['apple'])
#
mevalar = {'olma':10000,'tarvuz':8000,'qovun':10000}
print(f"Olmani narhi {mevalar['olma']} so'm")
#
# # Lug'atda istalgan ma'lumot turlarini saqlash mumkin !

talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
print(f"{talaba_0['ism'].title()},\
      {talaba_0['t_yil']}-yilda tug'ilgan,\
          {talaba_0['yosh']} yoshda")

# # Yangi kalit so'z va qiymat qo'shish
talaba_0['kurs'] = 4
talaba_0['fakultet'] = 'infornatika'
talaba_0['ism'] = 'abdulloh'
#
# # Bo'sh Lug'at
talaba_1 = {}
talaba_1['ism'] = 'qobul rasulov'
talaba_1['kurs'] = 3
talaba_1['yosh'] = 20
print(talaba_1)
print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")
#
# # kalit so'z-qiymat ni o'chiirib tashlash
talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
print(talaba_0)
del talaba_0['yosh']
print(talaba_0)
# 
# # Lu'gatlarni bir nechta qatorda yozsih
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'orif':'nokia 3310',
    'anvar':'pixel 3xl'
    }
#
# # get() - metodi lug'at ichidegi ma'lumotni olsh uchun metodi
meva = en_uz.get('pineapple', 'bunday meva mavjud emas')
print(meva)

























