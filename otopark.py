#1.soru
menu=0 #oncelikle degiskenlerimizi belirliyoruz
plaka=0
arac_sayisi=0
while True: #programımızın sürekli calısması icin donguye alıyoruz
    
    if menu==0:
        menu=int(input("MENU\n1-Arac Girisi\n2-Arac Cıkısı\n-1-Program Cıkısı\n"))
    elif menu==1:
        if arac_sayisi==20:
            print("Otoparkimiz doludur. Lutfen arac cikmasini bekleyin.")
            menu=0 #menuye sıfır degeri atayarak donguyu basa dondurmesini saglıyoruz
        else:
            plaka=input("Lütfen arada bosluk olmayacak sekilde plakanizi giriniz: ")
            arac_sayisi+=1 #arac girisi oldukca icerideki arac sayısını arttırıyoruz
            print("Hosgeldiniz. İcerideki arac sayisi: {}".format(arac_sayisi))
            menu=0
            
    elif menu==2: #otoparkta kalınan süreye gore ücret belirliyoruz
        plaka=input("arac plakanizi giriniz: ")
        saat=int(input("kac saat kaldiniz?: "))
        arac_sayisi-=1#arac cıkısı oldukca icerideki arac sayısını azaltıyoruz
        if saat==1:
            print("5TL odeyiniz.")
            print("İcerideki arac sayisi:{} ".format(arac_sayisi))
        elif saat==2:
            print("10TL odeyiniz.")
            print("İcerideki arac sayisi:{} ".format(arac_sayisi))
        elif saat==3:
            print("15TL odeyiniz.")
            print("İcerideki arac sayisi:{} ".format(arac_sayisi))
        else:
            print("40TL odeyiniz.")
            print("İcerideki arac sayisi:{} ".format(arac_sayisi))
        menu=0
    elif menu==-1:
        print("Programdan cikis yaptiniz. İyi günler dileriz.")
        quit()


