# # # 06  Dars STRING (matn)

name = "Doston"
shahar = "Jizzax"
viloyat = "Jizzax"
#
matn = "Men yangi 📱 oldim"
smayl = "😄"
#
ism = "Doston"
print("Mening ismim " + ism)
#
ism = 'Doston'
familiya = 'Kamolov'
print(ism + familiya)
print(ism + ' ' + familiya)

# # f-string 1-nechta matnlarni ozgaruvchi matinlarni birlashtiradi.
ism = 'Doston'
familiya = 'Kamolov'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif)
#
ism = 'Doston'
familiya = 'Kamolov'
print(f"Salom, mening ismim {ism}. {ism} {familiya}!")

# # Maxsus belgilar!

print("hello dosya!")
print("hello \tdosya!")  # \t - uzun bushliq qoldiradi #bta tab miqdordegi bushliq!
print("hello \ndosya!")  # \n - qator kochirish belgisi # bta qator pastga tushurb beradi !

# # String metodlar !

ism = 'doston'
familiya = 'kamolov'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.upper()) # upper() - metodi xama xarifni katalashtiradi !
print(ism_sharif.title()) # title() - metodi matndegi xar bta so'zni birinchi xarifini katta xarf bn yozadi !
print(ism_sharif.capitalize()) # capitalize - metodi matini faqatgina birinchi xarifini kata xarf bn yozadi !
#
meva = '    olma    '
print("Men "+ meva.lstrip() + " yaxshi ko'rama") # lstrip() - metodi chap tarafdagi bo'shliqni olib tashlaydi !
print("Men "+ meva.rstrip() + " yaxshi ko'rama") # rstrip() - metodi ung tarafdagi bp'shliqni olib tashlaydi !
print("Men "+ meva.strip() + " yaxshi ko'rama") # strip() - metodi ikki tarafdagi bo'shliqni olib tashaydi !
print("Men "+ meva + " yaxshi ko'rama")

# # Input - foydalanuvchidan malumot olish !

ism = input("Ismingiz nima?")
print("Assalomu alekum, " + ism)
#
ism = input("Ismingiz nima?/n>>>")
print("Assalomu alekum, " + ism.title())























