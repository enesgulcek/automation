# Dosya adını al
filename = input("Dosya adı: ")

# Dosyayı aç ve oku
with open(filename, "r") as file:
    text = file.read()

# Yeni satırları boşluk karakterine dönüştür
new_text = text.replace("\n", " ")

# Dosyayı yazdır
with open(filename, "w") as file:
    file.write(new_text)
