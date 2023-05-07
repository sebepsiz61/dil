from googletrans import Translator  # kütüphane eklenir

url = input("kelime giriniz  : ")  # genel olarak dil girilebilir
Translate = Translator()  # çeviri burada yapılıyor
cevir = Translate.translate(url, dest='tr')  # burda(dest'istediğimiz dil ') çevrilir
print(cevir.text)  # ekrana yazdırılır...

# googletrans
# py -m pip install "googletrans==4.0.0rc1"  sürümü yüklenmeli yoksa sürüm hata veriyor...
