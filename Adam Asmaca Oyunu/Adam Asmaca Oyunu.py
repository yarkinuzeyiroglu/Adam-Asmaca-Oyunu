while True:
    import random
    kelimeler = ["ders" , "teknoloji" , "merkez" , "sistem" , "bilim" , "ingilizce" , "kodlama" , "listeler" , "sözlük" , "string", "float","integer","python","pythonista","bilişim","film", "dizi","kitap"]
    kelime = random.choice(kelimeler) # Kelimler içerisinden rastgele bir kelime seçiliyor.
    tahminSayisi = 10 # Kullanıcının kaç kez tahmin edebileceğini belirtiyoruz.
    harfler = [] # Kullanıcının girdiği tüm harfleri bu listeye ekleyerek tekrar değer girdiği zaman uyarı vermesi sağlanacak.
    x = len(kelime) #Seçilen kelimenin uzunluğunu belirtip x değerinin içine atıyoruz.
    z = list('_' * x) # X uzunluğu kadar "_" ekliyoruz.
    print(' '.join(z), end='\n') #Alt tireler arasına boşluk ekliyoruz.
    while tahminSayisi > 0:
        y = input("Bir harf tahmin edin : ")
        if y in harfler:
            print("Lütfen daha önce tahmin ettiğiniz harfleri tekrar tahmin etmeyin!")
            continue
        elif len(y) > 1:
            tahminSayisi -= 1
            print("Lütfen sadece bir harf girin.{} tane tahmin hakkınız kaldı.".format(tahminSayisi))
            continue
        elif y not in kelime:   #Girilen harf kelime içinde yoksa yanlış bir değer girdiğini söylüyoruz.
            print("Yanlış Tahmin!")
        else:
            for i in range(len(kelime)):#Girilen harf kelime içerisinde değilse yanlış tahmin olduğunu söylüyoruz. 
                if y == kelime[i]:
                    print("Doğru Tahmin!")
                    z[i] = y
                    harfler.append(y)
            print(' '.join(z), end='\n')
        if y not in kelimeler:# Tahmin sayısına göre adamı asıyoruz.
            tahminSayisi = tahminSayisi - 1
            if tahminSayisi == 9:
                print("9 hakkınız kaldı!")
                print("  --------  ")
                print("     |")
            if tahminSayisi == 8:
                print("8 hakkınız kaldı!")
                print("  --------  ")
                print("     |")
                print("     O      ")
            if tahminSayisi == 7:
                print("7 hakkaınız kaldı!")
                print("  --------  ")
                print("     |      ")
                print("     O      ")
                print("     |     ")
            if tahminSayisi == 6:
                print("6 hakkınız kaldı!")
                print("  --------  ")
                print("     |       ")
                print("     O      ")
                print("     |      ")
                print("      \      ")
            if tahminSayisi == 5:
                print("5 hakkınız kaldı!")
                print("  --------  ")
                print("     |       ")            
                print("     O      ")
                print("     |      ")
                print("    / \   ")
            if tahminSayisi == 4:
                print("4 hakkınız kaldı!")
                print("  --------  ")
                print("     |       ")
                print("     O_     ")
                print("     |      ")
                print("    / \     ")
            if tahminSayisi == 3:
                 print("3 hakkınız kaldı!")
                 print("  --------  ")
                 print("     |")
                 print("    _O_   ")
                 print("     |      ")
                 print("    / \     ")
            if tahminSayisi == 2:
                 print("2 hakkınız kaldı!")
                 print("  --------  ")
                 print("     |")
                 print("    _O_   ")
                 print("     | \     ")
                 print("    / \     ")
            if tahminSayisi == 1:
                 print("1 hakkınız kaldı!")
                 print("  --------  ")
                 print("     |")
                 print("    _O_   ")
                 print("   / | \     ")
                 print("    / \     ")
            if tahminSayisi == 0:
                 print("Oyun bitti")
                 print("Geriye hiç hakkınız kalmadı")
                 print("  --------  ")
                 print("     |      ")
                 print("    _x_    ")
                 print("   / | \     ")
                 print("    / \     ")
                 break
        cevap = input("Kelimeyi buldunuz mu? ['E' veya 'H'] : ")#Kelimeyi her seferinde tahmin etme şansı tanıyoruz böylece kullanıcı kelimeyi bulursa direkt sona ulaşabilir.
        if cevap == "E":
            tahmin = input("Tahmin ettiğiniz kelime: ")
            if tahmin == kelime:
                print("Kazandınız!!!")
                break
            elif cevap == "H":
                tahminSayisi -= 1
                print("Yanlış tahmin ettiniz. {} tane tahmin hakkınız kaldı.".format(tahminSayisi))
            else:
                continue
    tekoyun = input("Tekrar Oyanamak İster Misiniz? (e/h):" )          
    if "e" == tekoyun :
        False
    elif "h" == tekoyun : 
        True
        break
    else:
        print("Lütfen sadece evet için e, hayır için h harflerini giriniz")
        break
