dosya_adı = input("Dosya adı: ")
aranan_metin = input("Aranacak metin: ")

with open(dosya_adı, "r") as dosya:
    for satir in dosya:
        if aranan_metin in satir:
            print(satir)
