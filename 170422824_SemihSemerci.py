import numpy as np

def Rezervasyon(salon):
    global biletAdedi, sayac
    metin = open("Fiyat Bilgisi.txt", "r")
    FiyatListesi = []
    for i in metin:
        temp = i.strip()
        FiyatListesi.append(temp.split("-"))
    rezerve = []
    kategori = int(input("Katogori giriniz:(1-4)"))
    if kategori>0 and kategori<5:
        biletAdedi = int(input("Bilet adedi giriniz:(1-" + FiyatListesi[0][1] + ")"))
        sayac = 0
    else:
        print("Hatalı giris")
    if kategori == 1:
        if biletAdedi <= int(FiyatListesi[0][1]):
            for i in range(0, 10):
                for j in range(5, 15):
                    if salon[i][j] == 0:
                        rezerve.append(i)
                        rezerve.append(j)
                        sayac = sayac + 1
                        salon[i][j] = 1
                    elif sayac == biletAdedi:
                        break

                if sayac == biletAdedi:
                    break

            print("Alınan biletler:")
            for i in range(0, len(rezerve) - 1, 2):
                if (rezerve[i]+1==10) and (rezerve[i + 1]+1==15):
                    print((rezerve[i] + 1), "-", (rezerve[i + 1] + 1))
                    print(kategori,". kategori dolmuştur daha fazla alamazsınız")
                else:
                    print((rezerve[i]+1),"-",(rezerve[i + 1]+1))

            TutarHesapla(FiyatListesi, biletAdedi, kategori)
            rezerve.clear()
        else:
            print("En fazla " + FiyatListesi[0][1] + " tane bilet alabilirsiniz!")

    elif (kategori == 2):

        liste = [4, 3, 2, 1, 0, 15, 16, 17, 18, 19]
        sayac = 0
        if biletAdedi <= int(FiyatListesi[0][1]):
            for i in range(0, 10):
                for j in liste:
                    if salon[i][j] == 0:
                        rezerve.append(i)
                        rezerve.append(j)
                        sayac = sayac + 1
                        salon[i][j] = 1

                        if sayac == biletAdedi:
                            break
                if sayac == biletAdedi:
                    break

            print("Alınan biletler:")
            for i in range(0, len(rezerve) - 1, 2):
                if (rezerve[i]+1==10) and (rezerve[i + 1]+1==20):
                    print((rezerve[i] + 1), "-", (rezerve[i + 1] + 1))
                    print(kategori,". kategori dolmuştur daha fazla alamazsınız")
                else:
                    print((rezerve[i]+1),"-",(rezerve[i + 1]+1))

            TutarHesapla(FiyatListesi, biletAdedi, kategori)
            rezerve.clear()
        else:
            print("En fazla " + FiyatListesi[0][1] + " tane bilet alabilirsiniz!")

    elif kategori == 3:
        if biletAdedi <= int(FiyatListesi[0][1]):
            for i in range(10, 20):
                for j in range(5, 15):
                    if salon[i][j] == 0:
                        rezerve.append(i)
                        rezerve.append(j)
                        sayac = sayac + 1
                        salon[i][j] = 1
                        if sayac == biletAdedi:
                            break
                if sayac == biletAdedi:
                    break
            print("Alınan biletler:")
            for i in range(0, len(rezerve) - 1, 2):
                if (rezerve[i]+1==20) and (rezerve[i + 1]+1==15):
                    print((rezerve[i] + 1), "-", (rezerve[i + 1] + 1))
                    print(kategori,". kategori dolmuştur daha fazla alamazsınız")
                else:
                    print((rezerve[i]+1),"-",(rezerve[i + 1]+1))

            TutarHesapla(FiyatListesi, biletAdedi, kategori)
            rezerve.clear()
        else:
            print("En fazla " + FiyatListesi[0][1] + " tane bilet alabilirsiniz")

    elif (kategori == 4):
        liste = [4, 3, 2, 1, 0, 15, 16, 17, 18, 19]
        sayac = 0
        if biletAdedi <= int(FiyatListesi[0][1]):
            for i in range(10, 20):
                for j in liste:
                    if salon[i][j] == 0:
                        rezerve.append(i)
                        rezerve.append(j)
                        sayac = sayac + 1
                        salon[i][j] = 1

                        if sayac == biletAdedi:
                            break
                if sayac == biletAdedi:
                    break
            print("Alınan biletler:")
            for i in range(0, len(rezerve) - 1, 2):
                if (rezerve[i]+1==20) and (rezerve[i + 1]+1==20):
                    print((rezerve[i] + 1), "-", (rezerve[i + 1] + 1))
                    print(kategori,". kategori dolmuştur daha fazla alamazsınız")
                else:
                    print((rezerve[i]+1),"-",(rezerve[i + 1]+1))

            TutarHesapla(FiyatListesi, biletAdedi, kategori)
            rezerve.clear()
        else:
            print("En fazla " + FiyatListesi[0][1] + " tane bilet alabilirsiniz")

def SalonYazdir(salon):
    for i in range(0, 20):
        for j in range(0, 20):
            if (salon[i][j] == 0):
                print("-", end="")
            else:
                print("X", end="")
        print()

def YeniEtkinlik(salon):
    for i in range(0, 20):
        for j in range(0, 20):
            if (salon[i][j] == 1):
                salon[i][j] = 0

    print("Yeni etkinlik oluşturuldu")
    for i in range(0, 20):
        for j in range(0, 20):
            print("-", end="")
        print()
    Ciro.clear()

def TutarHesapla(FiyatListesi, biletAdedi, kategori):
    indirim = 0
    fiyat = 0
    for i in range(1, 5):
        if kategori == int(FiyatListesi[i][0]):
            fiyat = int(FiyatListesi[i][1])
        elif kategori == int(FiyatListesi[i][0]):
            fiyat = int(FiyatListesi[i][1])
        elif kategori == int(FiyatListesi[i][0]):
            fiyat = int(FiyatListesi[i][1])
        elif (kategori == int(FiyatListesi[i][0])):
            fiyat = int(FiyatListesi[i][1])

    tempFiyat = fiyat
    for i in range(5, len(FiyatListesi)):
        if int(FiyatListesi[i][0]) == kategori:
            if (FiyatListesi[i][2]) == "M":
                (FiyatListesi[i][2]) = FiyatListesi[0][1]
                if biletAdedi >= int(FiyatListesi[i][1]) and biletAdedi <= int(FiyatListesi[i][2]):
                    fiyat = fiyat - (fiyat * int(FiyatListesi[i][3])) // 100
                    indirim = int(FiyatListesi[i][3])

            elif biletAdedi >= int(FiyatListesi[i][1]) and biletAdedi <= int(FiyatListesi[i][2]):
                fiyat = fiyat - (fiyat * int(FiyatListesi[i][3])) // 100
                indirim = int(FiyatListesi[i][3])

    indirimliFiyat = fiyat * biletAdedi
    Ciro.append(indirimliFiyat)

    print("Toplam fiyat:", (tempFiyat * biletAdedi))
    print("İndirimli fiyat:", indirimliFiyat)
    print("İndirim oranınız:%", indirim)

def CiroHesapla():
    toplam = 0
    for i in Ciro:
        toplam += i
    return toplam


salon = np.zeros((20, 20), dtype=int)
Ciro = []

while True:
    print("******MENÜ******\n1.Rezervasyon\n2.Salonu Yazdır\n3.Yeni Etkinlik\n4.Ciro Hesapla\n0.Çıkış\n------------")
    secim = int(input("Seçiminiz:"))
    if secim == 1:
        Rezervasyon(salon)
    elif secim == 2:
        SalonYazdir(salon)
    elif secim == 3:
        YeniEtkinlik(salon)
    elif secim == 4:
        print("Ciro:", CiroHesapla())
    elif secim == 0:
        print("Çıkış yapılıyor...")
        break
    else:
        print("Hatalı giriş")
