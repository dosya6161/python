# # # 19-dars: FUNCTIONS (FUNKSIYALAR)

def salom_ber(): # funksiya yaratishda def operator bn boshlemiz 
    """Salom beruvchi funksiya"""
    print("Assalomu alaykum!")

salom_ber()

#
def salom_ber(ism):
    """Fodyalanuvchi ismini qabul qilib, 
    unga salom beruvchi funksiya"""
    print(f"Assalomu alaykum, hurmatli {ism.title()}!")

salom_ber('Doston')
salom_ber('Farrux')

# salom_ber()
# .__doc__ funksiyani nima qilishini korsatadi, malumotini kursatadi

def yosh_hisobla(tugilgan_yil, joriy_yil):
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

yosh_hisobla(1995,2020)
yosh_hisobla(1993)

# tyil = input("Tug'ilgan yilingizni kiriting: ")
# yosh_hisobla(tyil)