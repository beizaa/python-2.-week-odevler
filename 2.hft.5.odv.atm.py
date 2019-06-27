#ATM ile bankadan para cekmeyi saglayan bir program.


print("""ATM-- Islemler: (1) bakiye kontrolu
                (2) para yatirma
                (3) para cekme

""")
#1 ile bakiye kontrolu
#2 ile para yatirma ve
#3 ile de para cekme islemi yapiyoruz.

while True:

    islem=input("Hangi islemi yapmak istediginizi seciniz.")
    hesapta_bulunan_para= int(1000) 

    if islem=="1":
        print("Hesabinizda", hesapta_bulunan_para, "Euro para bulunmaktadir.")
        

    elif islem=="2":
        yatirilmak_istenen_para=int(input("Ne kadar para yatirmak istiyorsunuz?"))
        print("Hesabiniza", yatirilmak_istenen_para, "Euro para yatirildi.")
        print("Yeni bakiyeniz=", hesapta_bulunan_para+yatirilmak_istenen_para)
    elif islem=="3":
        cekmek_istediginiz_tutar=int(input("Cekmek istediginiz tutar nedir?"))
        print("Hesabinizdan", cekmek_istediginiz_tutar, "Euro cekilmistir.")
        print("Kalan bakiyeniz=", hesapta_bulunan_para-cekmek_istediginiz_tutar)

        if cekmek_istediginiz_tutar>1000:
            print("Bakiyeniz yetersiz!")
    elif not islem:
        break
        

#1. Program calisiyor.
#2. Acik sanirim yok
#3. Mantik hatasi var. Parayi guncel tutamiyorum. Yani bir islem yapinca mesela para yatirdim yeni paraniz 1100 diyor ama sonra cekme islemini yine 100 uzerinden yapiyor.
#Hocama danistigima gore bunun icin sayac gerekiyormus ama nasil yapcagimi bilemedim.
#4.Degisken isimleri acik diye dusunuyorum.
#5.Anlasilir.
#6.Bence yeterince kisa.
#7. Yorum eklenmis.
#8. Algoritma mantikli ama sayac kismi eksik.
#9.Kapsamli ama parayi guncel tutma kismi eksik kalmis.


