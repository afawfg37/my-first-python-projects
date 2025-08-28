import os
import shutil
import time
import random
import webbrowser
bilgiler=[
    # Bilim ve Teknoloji (1-20)
    "Dünya, güneş etrafında saatte yaklaşık 107.000 km hızla döner.",
    "İnsan beyni yaklaşık 1.4 kg ağırlığındadır.",
    "DNA’nın toplam uzunluğu bir hücrede yaklaşık 2 metreye eşittir.",
    "Elektronlar, atomun çekirdeği etrafında saniyede milyonlarca tur atar.",
    "Güneş ışığı Dünya’ya 8 dakika 20 saniyede ulaşır.",
    "İlk bilgisayar 1940’larda yapıldı ve mekanik çalışıyordu.",
    "Python dili 1991’de Guido van Rossum tarafından yaratıldı.",
    "İnsan gözünün çözünürlüğü yaklaşık 576 megapiksel gibi hesaplanır.",
    "Dünyadaki suyun %97’si tuzlu sudur.",
    "Karıncalar, kendi ağırlıklarının 50 katını taşıyabilir.",
    "Kuantum bilgisayarlar klasik bilgisayarlardan tamamen farklı çalışır.",
    "Evrenin yaşı yaklaşık 13.8 milyar yıldır.",
    "Ay’ın yüzeyinde yerçekimi Dünya’nın yaklaşık altıda biri kadardır.",
    "İlk programcı, Ada Lovelace olarak bilinir.",
    "İnsan kalbi günde yaklaşık 100.000 kez atar.",
    "Bir light year (ışık yılı) ışığın bir yılda aldığı mesafedir.",
    "Karbon atomları tüm organik yaşamın temel yapı taşlarıdır.",
    "İnsan vücudunda 60.000 km uzunluğunda damar vardır.",
    "Evrenin %68’i karanlık enerjiden oluşur.",
    "3D printerlar metal, plastik ve organik doku yazdırabilir.",

    # Tarih ve Kültür (21-40)
    "İlk yazılı kanunlar M.Ö. 1754’de Hammurabi tarafından yazıldı.",
    "Piramitler, Mısır’da 4500 yıl önce inşa edildi.",
    "Matbaanın icadı 1440’larda Johannes Gutenberg’e aittir.",
    "İlk olimpiyat oyunları M.Ö. 776’da Yunanistan’da yapıldı.",
    "Marco Polo, 13. yüzyılda Asya’yı Avrupa’ya tanıttı.",
    "Osmanlı İmparatorluğu 600 yıl hüküm sürdü.",
    "Magna Carta 1215’te İngiltere’de kralın yetkilerini sınırladı.",
    "Rönesans dönemi, 14-17. yüzyıllarda Avrupa’da sanatı ve bilimi geliştirdi.",
    "Vikipedi 2001’de kuruldu.",
    "Dünya Savaşı I (1914-1918), 20 milyon insanın ölümüne sebep oldu.",
    "Ayasofya 537 yılında tamamlandı.",
    "İnka İmparatorluğu, Güney Amerika’da geniş bir medeniyet kurdu.",
    "İlk telefon, Alexander Graham Bell tarafından icat edildi.",
    "Christopher Columbus 1492’de Amerika’ya ulaştı.",
    "Leonardo da Vinci, Mona Lisa’yı 1503’te yapmaya başladı.",
    "İlk radyo yayını 1906’da yapıldı.",
    "Fransa’da Bastille Hapishanesi 1789’da alındı.",
    "Çin Seddi, M.Ö. 7. yüzyıldan itibaren inşa edildi.",
    "İlk uzay aracı Sputnik, 1957’de fırlatıldı.",
    "Modern olimpiyat bayrağı 1913’te tasarlandı.",

    # Doğa ve Evren (41-60)
    "Plüton artık resmi olarak gezegen kabul edilmiyor.",
    "Jüpiter’in manyetik alanı Dünya’nın 20.000 katıdır.",
    "Dünyadaki volkanların %75’i su altındadır.",
    "Balinalar memeli olmasına rağmen su altında yaşar.",
    "Şimşek saniyede 30.000 Kelvin sıcaklığa ulaşabilir.",
    "Karıncalar topluluk halinde çalışarak kendi kolonilerini yönetir.",
    "Amazon Nehri, hacim açısından dünyanın en büyük nehridir.",
    "Güneş’in merkez sıcaklığı yaklaşık 15 milyon °C’dir.",
    "Satürn’ün halkaları buz ve taş parçalarından oluşur.",
    "İnsan genleri %98 oranında şempanzelerle aynıdır.",
    "Deniz yıldızlarının beyni yoktur.",
    "Mercan resifleri, okyanusların en zengin ekosistemlerindendir.",
    "Yıldırım yılda ortalama 1.4 milyar kez düşer.",
    "Ay, Dünya’ya göre gittikçe uzaklaşıyor (yılda 3.8 cm).",
    "Kutup ayıları beyaz değil, tüyleri şeffaftır.",
    "Dünya’nın en derin noktası Mariana Çukuru’dur (yaklaşık 11 km).",
    "Böcekler tüm hayvan türlerinin %80’ini oluşturur.",
    "Kuzey ışıkları, Güneş’ten gelen yüklü parçacıklarla oluşur.",
    "Dev ahtapotların gözleri bir insan gözü büyüklüğündedir.",
    "Biyolüminesans, deniz canlılarının kendi ışıklarını üretmesidir.",

    # Genel Kültür, İnsan ve Teknoloji (61-100)
    "Plüton artık resmi olarak gezegen değil, cüce gezegen kabul edilir.",
    "İnsan DNA’sının %99,9’u tüm insanlarda aynıdır.",
    "Bir ahtapotun üç kalbi vardır.",
    "Dünya’nın atmosferi %78 azot, %21 oksijen içerir.",
    "Kediler insanların kalp atışlarını hissedebilir.",
    "İlk yazılı efsaneler Sümerler tarafından yaratıldı.",
    "Bilgisayar virüsleri ilk kez 1986’da ortaya çıktı.",
    "İnsan vücudu her gün yaklaşık 1 litre mukus üretir.",
    "Dünya üzerinde bilinen en eski ağaç yaklaşık 5000 yaşındadır.",
    "Süpernova patlamaları Güneş’ten milyarlarca kat enerji açığa çıkarır.",
    "Einstein, 1921’de Nobel Fizik Ödülü’nü aldı.",
    "İnsan vücudundaki toplam kemik sayısı 206’dır.",
    "Dünya’nın manyetik kutupları zamanla yer değiştirir.",
    "Güneş sistemi, Güneş ve 8 gezegenden oluşur.",
    "İlk elektronik bilgisayar ENIAC 1945’te tamamlandı.",
    "İnsan gözleri, mavi ışığa diğer renklere göre daha duyarlıdır.",
    "Dünyadaki tüm karıncaların toplam ağırlığı insanların toplam ağırlığına yakındır.",
    "İlk uzay yürüyüşü 1965’te yapıldı.",
    "İnsan vücudu, her gün yaklaşık 2 litre tükürük üretir.",
    "Ay’da rüzgar olmadığı için izler yıllarca kalır.",
    "Böcekler, tür olarak tüm hayvanların %80’ini oluşturur.",
    "Amazon ormanı, Dünya oksijeninin %20’sini üretir.",
    "İlk yazılı matematik sistemleri M.Ö. 3000 civarında Sümerlerde bulundu.",
    "Dünya’nın en büyük çölü Antarktika’dır.",
    "Güneş, yaklaşık 4.6 milyar yıl önce oluştu.",
    "Bir yılda, Dünya yaklaşık 940 milyon km yol kateder.",
    "İnsan vücudunda yaklaşık 37 trilyon hücre vardır.",
    "Tardigradlar (su ayıları) uzayda hayatta kalabilir.",
    "Dünya’daki en büyük canlı mantar, 965 hektarlık alana yayılır.",
    "İlk programlama dili, Ada Lovelace tarafından oluşturuldu.",
    "İnsan saçları ayda ortalama 1 cm uzar.",
    "Bal arıları, dans ederek iletişim kurar.",
    "Beyin, vücut ağırlığının %2’sini oluşturur ama enerji tüketiminin %20’sini harcar.",
    "Dünya’nın en yüksek dağı Everest’tir (8.848 m).",
    "Titanik 1912’de battı.",
    "İlk yapay uydu Sputnik 1957’de fırlatıldı.",
    "Dünya’nın en büyük okyanusu Pasifik Okyanusu’dur.",
    "Deniz seviyesinde su kaynama noktası 100 °C’dir.",
    "İlk uzay aracı Ay’a insan taşıdı: Apollo 11 (1969).",
    "Bir fırtınadaki yıldırımın sıcaklığı 30.000 K’ye ulaşabilir.",
    "Dünyadaki en uzun nehir Nil Nehri’dir.",
    "İnsan vücudu günde yaklaşık 2-3 litre su kaybeder.",
    "Bir kum tanesi yaklaşık 1 milyon atom içerir.",
    "Dünya’nın manyetik alanı hayvanların göçünde yön bulmalarını sağlar.",
    "Beyin, saniyede yaklaşık 100 trilyon işlem yapabilir.",
    "İnsan bağırsağı yaklaşık 7 metre uzunluğundadır.",
    "Deniz kaplumbağaları, yönlerini Dünya’nın manyetik alanından bulur.",
    "İlk elektrikli araba 1828’de icat edildi.",
    "Bir yılda, Dünya yaklaşık 365,25 gün döner.",
    "Karıncaların çoğu kendi ağırlığının 50 katını taşıyabilir.",
    "İlk hava uçağı Wright kardeşler tarafından 1903’te uçuruldu.",
    "Güneş’in yüzeyi yaklaşık 5.500 °C sıcaklıktadır.",
    "Bir insanın DNA’sındaki baz çiftlerinin sayısı yaklaşık 3 milyar.",
    "Dünya’nın en uzun köprüsü DanyangKunshan Grand Köprüsü’dür."

]

def dosya_olustur():
    dosya_isim = input("Oluşturulacak dosyanın ismi: ").strip()
    try:
        os.mkdir(dosya_isim)
        print(f"{dosya_isim} adlı dosya oluşturuldu. Mevcut dizin:", os.listdir())
    except FileExistsError:
        print("Bu isimde bir dosya/dizin zaten mevcut!")

def dosya_sil():
    dosya_isim_remove = input("Silmek istediğiniz dosyanın ismi: ").strip()
    eminlik = input("Emin misiniz? (e/h): ").lower().strip()
    if eminlik == "e":
        try:
            shutil.rmtree(dosya_isim_remove)
            print(f"{dosya_isim_remove} dosyası/dizini temizlendi.")
        except FileNotFoundError:
            print("Böyle bir dosya/dizin bulunamadı.")
    else:
        print("İşlemden vazgeçildi.")

def hesap_makinesi():
    

    sayi1=float(input("İlk sayıyı yazınız: "))
    sayi2=float(input("Diğer sayıyı da yazın: "))
    islem_tür=input("hangi işlem türünü seçiyorsun toplama için(+),çıkarma için(-),çarpma(*),bölme(/): ").lower().strip()
    if islem_tür=="+":
        print("Sonuç: ",sayi1+sayi2)
    elif islem_tür=="-":
        print("Sonuç: ",sayi1-sayi2)
    elif islem_tür=="*":
        print("Sonuç: ",sayi1*sayi2)
    elif islem_tür=="/":
        print("Sonuç: ",sayi1/sayi2)
    else:
        print("İşlem türü bulunamadı")

    
def internet():
    

    istek_web=input("Hangi web sitesine girmek istiyorsan tam urlsini yaz: ").lower().strip()
    print("Yükleniyor...")
    time.sleep(1)
    webbrowser.open(istek_web)
def cahilsavar():
    

    
    giriş1=input("Bilgilenmek için (b) cahil kalmak için(c): ").lower().strip()
    print("Düşünüyor")
    time.sleep(1)
    print("Al bilgi: ",random.choice(bilgiler))
    if giriş1=="c":
        print("yinede cahil kalma!")
def oyun():
    
 while True:
     
  oyunsec=input("kumar(kumar),sayı_tahmin(tahmin): ")
  if oyunsec=="kumar":
        
    yatırım=int(input("Yatırılacak tutarı seç: "))
    time.sleep(0.5)
    tahmin=int(input("Tahminin kaç 1,100 arası: "))
    tutulan_sayi=random.randint(1,100)
    kazanç=yatırım*4
    if tahmin==tutulan_sayi:
        print("Kazandın",kazanç,"TL")
    else:
        print("Gitti paracıklar")
    if oyunsec=="tahmin":
        asıl_sayi=random.randint(1,101)
        tutmak=int(input("Bir sayı söyle: "))
        if tutmak==asıl_sayi:
            print("Kazandın")
            
        elif tutmak<asıl_sayi:
            print("tahminin fazla küçük")
        elif tutmak>asıl_sayi:
            print("tahminin fazla büyük")
    
        
    
    
            
    
    
while True:    
 print("Diken OS'a hoş geldiniz")
 time.sleep(0.2)
 try:
     giriş=input("ne yapmak istersiniz internete girmek için(w),dosya oluşturmak için(d),dosya silmek için(ss),mini oyunlar için(g),hesap makinesi için(/*-),bilgilenmek için(cahildoksit): ").lower().strip()
     if giriş=="w":
         internet()
     elif giriş=="d":
         dosya_olustur()
     elif giriş=="ss":
         dosya_sil()
     elif giriş=="/*-":
         hesap_makinesi()
     elif giriş=="cahildoksit":
         cahilsavar()
     elif giriş=="g":
         oyun()
 except(ValueError,IndentationError,ZeroDivisionError,EOFError,MemoryError):
    print("Sistemsel bir hata var")
         
         
     
 

