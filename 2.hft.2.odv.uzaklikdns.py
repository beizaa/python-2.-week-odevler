#Mesafeleri 'km' ve 'mil' cinsinden birbirine donusturmek icin bir program.

#Kilometreden mile cevirme formulu su sekildedir: 1 Kilometer= 0.621 mile

#Kullanicidan cevirilecek mesafe tipi ve uzunlugunu alarakk islemleri yapabiliriz.

print("""
@@@****The uzaklik birimi donusturucu****@@@
""")

donusum_tipi= input("Km-mil donusumu mu mil-km donusumu mu yapmak istiyorsunuz?")
mesafe= int(input("Donusturmek istediginiz birimin uzunlugunu giriniz."))

if donusum_tipi=="km-mil":
    print(mesafe, "km =", mesafe*0.621, "mil")
    
elif donusum_tipi=="mil-km":
    print(mesafe, "mil =", mesafe/0.621, "km")
                     
