#Sayi tahmin oyunu

#Aklimdan bir sayi tuttum ve kullanici bu sayiyi bilmek icin hamleler yapiyor.

#Ilk seferde dogru bilirse 3 yildiz alacak.

#Ucuncu seferde dogru bilirse 2 yildiz alacak.

#Besinci seferde dogru bilirse 1 yildiz alacak.

aklimdaki_sayi = 5

print("Aklimdan bir sayi tuttum.")
a=1
while a==1:
    tahmin=input("Lutfen 1 ile 10 arasinda bir sayi tahmin edin.")

    if aklimdaki_sayi==5:
        print("Tebrikler, ilk denemede bildiniz! ★★★")
        break
while a==1:
    if aklimdaki_sayi==10:
        print("Bilemediniz, tekrar bir sayi tahmin edin.")
    elif aklimdaki_sayi==1:
        print("Yine olmadi, tekrar bir sayi tahmin edin.")
    elif aklimdaki_sayi==7:
        print("Maalesef, tekrar bir sayi tahmin edin.")
    elif aklimdaki_sayi==2:
        print("Uzgünüz. tekrar bir sayi tahmin edin.")
    
sayac=0
while sayac==1:
    print("Tebrikler. besinci denemede bildiniz. ★")
while sayac==3:
    print("Tebrikler üçüncü denemede bildiniz. ★★")

#Internetten arastirdigimda su tarz seyler cikti:
# <<<<<<<while aklimdaki_sayi != tahmin and attempts < 6>>>>>>>>>>
#Bence sayac kullanmaliydim. Ama nasil kullancagimi bilemedim.
#1. yanlis calisiyor, cunku yapamadim.
#2. acik sanirim yok
#3. Mantik hatasi var. 5 yazinca tebrik etmesi lazim, 3 yazinca da ediyor, buldunuz diyor.
#Ayni zamanda ilkinda bildiniz, ucuncude bildiniz, besincide bildiniz olayini yapamadim, sayac lazim galiba bilmiyorum.
#4.Degisken isimleri acik diye dusunuyorum.
#5.Sonlara dogru anlasilmazlasiyor.
#6.Kisa, olmasi gerekenden de kisa sanirim.
#7. Yorum eklenmis.
#8. Algoritma mantikli ama yarim kalmis.
#9.Maalesef kapsamli degil.
        
   
