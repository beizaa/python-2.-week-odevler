#burclari ogrenmek icin bir python programi
#Feedback son tarafta.

print("Burc ogrenme, hosgeldiniz!!!")

dogum_ayi=input("Dogdugunuz ayi giriniz:")
dogum_gun=int(input("Dogdugunuz gunu giriniz:")) 
if dogum_ayi=="Mart":
    if dogum_gun>21:
        print(dogum_gun, dogum_ayi, "tarihinde dogan birinin burcu koc olmali.")
    else:
        print(dogum_gun, dogum_ayi, "tarihinde dogan birinin burcu balik olmali.")

if dogum_ayi=="Nisan":
    if dogum_gun>21:
        print(dogum_gun, dogum_ayi, "tarihinde dogan birinin burcu boga olmali.")
    else:
        print(dogum_gun, dogum_ayi, "tarihinde dogan birinin burcu koc olmali.")

if dogum_ayi=="Mayis":
    if dogum_gun>22:
        print(dogum_gun, dogum_ayi, "tarihinde dogan birinin burcu ikizler olmali.")
    else:
        print(dogum_gun, dogum_ayi, "tarihinde dogan birinin burcu boga olmali.")

if dogum_ayi=="Haziran":
    if dogum_gun>23:
        print(dogum_gun, dogum_ayi, "tarihinde dogan birinin burcu yengec olmali.")
    else:
        print(dogum_gun, dogum_ayi, "tarihinde dogan birinin burcu ikizler olmali.")

if dogum_ayi=="Temmuz":
    if dogum_gun>23:
        print(dogum_gun, dogum_ayi, "tarihinde dogan birinin burcu aslan olmali.")
    else:
        print(dogum_gun, dogum_ayi, "tarihinde dogan birinin burcu yengec olmali.")

if dogum_ayi=="Agustos":
    if dogum_gun>23:
        print(dogum_gun, dogum_ayi, "tarihinde dogan birinin burcu basak olmali.")
    else:
        print(dogum_gun, dogum_ayi, "tarihinde dogan birinin burcu aslan olmali.")

if dogum_ayi=="Eylul":
    if dogum_gun>23:
        print(dogum_gun, dogum_ayi, "tarihinde dogan birinin burcu terazi olmali.")
    else:
        print(dogum_gun, dogum_ayi, "tarihinde dogan birinin burcu basak olmali.")

if dogum_ayi=="Ekim":
    if dogum_gun>23:
        print(dogum_gun, dogum_ayi, "tarihinde dogan birinin burcu akrep olmali.")
    else:
        print(dogum_gun, dogum_ayi, "tarihinde dogan birinin burcu terazi olmali.")

if dogum_ayi=="Kasim":
    if dogum_gun>22:
        print(dogum_gun, dogum_ayi, "tarihinde dogan birinin burcu yay olmali.")
    else:
        print(dogum_gun, dogum_ayi, "tarihinde dogan birinin burcu akrep olmali.")

if dogum_ayi=="Aralik":
    if dogum_gun>22:
        print(dogum_gun, dogum_ayi, "tarihinde dogan birinin burcu oglak olmali.")
    else:
        print(dogum_gun, dogum_ayi, "tarihinde dogan birinin burcu yay olmali.")

if dogum_ayi=="Ocak":
    if dogum_gun>22:
        print(dogum_gun, dogum_ayi, "tarihinde dogan birinin burcu kova olmali.")
    else:
        print(dogum_gun, dogum_ayi, "tarihinde dogan birinin burcu oglak olmali.")

if dogum_ayi=="Subat":
    if dogum_gun>20:
        print(dogum_gun, dogum_ayi, "tarihinde dogan birinin burcu balik olmali.")
    else:
        print(dogum_gun, dogum_ayi, "tarihinde dogan birinin burcu kova olmali.")

  
        
#1. Calisiyor, ama burcu soylemiyor su anda. Gun icinde burclari cikti veriyordu. Yuklemeyi son ana biraktigim icin su anda duzeltmeyi yapamiyorum.
#2. Bug yok (varmis)
#3. Mantik hatasi yok. Sadece yakin tarihleri tam tersi yazmisim. yani once ayin genelde 22sinden sonrasini soyluyor,
#sonra  oncesini soyluyor.
#4.Degisken isimleri acik diye dusunuyorum.
#5.Bence anlasilir bir kod.
#6.Bilgim dahilinde olmasi gereken uzunlukta.
#7. Yorum eklenmis.
#8. Algoritma mantikli.
#9.Kapsamli.
