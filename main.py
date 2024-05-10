# random kütüphanesi kullanın
import random
# Kullanıcının parolasının içerebileceği tüm karakterleri içeren bir değişken oluşturun
karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
# Bir değişken oluşturun ve kullanıcıdan parolanın uzunluğunu girmesini isteyin
uzunluk = int(input("Şifrenizin Uzunluğunu giriniz: ")) 
# Programın oluşturulan parolayı saklayacağı bir değişken oluşturun
parola = ""
# Karakter değişkeninden rastgele bir karakter seçmek 
for i in range(uzunluk):
    # bunu oluşturulan  parolanın bulunduğu değişkene eklemek için bir döngü
    parola += random.choice(karakter)
# Elde edilen parolayı konsola yazdırın
print(parola)
    
    
