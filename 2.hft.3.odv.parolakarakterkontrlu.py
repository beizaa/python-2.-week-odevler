print("Parola karakter kontrolu")

a=1
while a==1:
    username= input("Lutfen en az 3 en fazla 18 karakterden olusan bir kullanici adi giriniz(Cikmak icin 'Seyhim beni isinla'):")

    if username == "Seyhim beni isinla":
        print("cikiliyor...")
        a=0
    elif len(username)<3:
        print("Kullanici adiniz 3 karakterden az olamaz!")
    elif len(username)>18:
        print("Kullanici adiniz 18 karakterden fazla olamaz!")
    else:
        print("Kullanici adi kabul edildi.")
        break

while a==1:
    parola= input("Lutfen bir parola belirleyiniz:")

    if len(parola)<6:
        print("Parolaniz 6 karakterden daha az olamaz!")
    elif len(parola)>12:
        print("Parolaniz 12 karakterden fazla olamaz!")
    else:
        print("Parolaniz kabul edildi.")
        break
if 18>len(username)>3 and 6<len(parola)<12:
    f= open("username_ve_parola.txt", "w")
    print("Username=", username, file=f)
    print("Parola=", parola, file=f)
    print("Bilgileriniz basariylla kaydedildi.", file=f)
    print("Username=", username)
    print("Parola=", parola)
    print("Bilgileriniz dosyaya kaydediliyor...")
    f.close()





                
