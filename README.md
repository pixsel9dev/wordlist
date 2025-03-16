🔥Wordpy

# 🚀Wordlist Oluşturucu

Bu program, kullanıcıdan alınan kelime ve rakamlarla **devasa ve detaylı bir wordlist** oluşturmanızı sağlar.  
İster **terminal argümanlarıyla**, ister **etkileşimli modda** kullanabilirsiniz!  

---

## 🔥 Özellikler (Features)
✅ **Gelişmiş Kombinasyonlar:** İsimler, soyisimler, doğum tarihleri, özel kelimeler, rakamlar ve karakterler ile **devasa kombinasyonlar** oluşturur.  
✅ **Etkileşimli Mod:** Terminalden **sorulara yanıt vererek** kolayca wordlist oluşturabilirsiniz.  
✅ **Hızlı ve Optimize Çalışma:** `itertools.product` kullanarak **maksimum hız** ile wordlist üretir.  
✅ **Özelleştirilebilir Uzunluk:** **Min - Max uzunluk** belirleyerek tam ihtiyacınıza uygun wordlist oluşturabilirsiniz.  
✅ **Tam Otomatik ve Hatasız:** Eksik parametreler varsa uyarı verir, **tam otomatik** çalışır.  

---

## 📌 Kurulum (Installation)
```sh
git clone https://github.com/pixsel9dev/wordlist.git
cd worldlist-main
pip install -r requirements.txt  # Gerekli paketleri yükleyin
🚀 Kullanım (Usage)
🔹 Terminal Modu
Tüm parametreleri belirleyerek direkt çalıştırabilirsiniz:


python wordlist.py -n Ali Ayşe -sn Yılmaz Demir -b 1990 2000 -k admin hacker -nu 123 456 -s @ # -cw araba ev -min 3 -max 6 -o mywordlist.txt
📌 Parametre Açıklamaları:

Parametre	Açıklama
-n veya --names	İsimler (Ali, Ayşe, Mehmet vb.)
-sn veya --surnames	Soyisimler (Yılmaz, Demir vb.)
-b veya --birthdays	Doğum tarihleri (1990, 2000 vb.)
-k veya --keywords	Anahtar kelimeler (admin, hacker vb.)
-nu veya --numbers	Sayılar (123, 456 vb.)
-s veya --special_chars	Özel karakterler (@, #, $ vb.)
-cw veya --custom_words	Ekstra kelimeler (araba, ev vb.)
-min veya --min_len	Minimum kombinasyon uzunluğu
-max veya --max_len	Maksimum kombinasyon uzunluğu
-o veya --output	Wordlist'in kaydedileceği dosya adı
🔹 Etkileşimli Mod
Komut satırında sorulara yanıt vererek wordlist oluşturabilirsiniz:


python wordlist.py -e
Bu modda size sorular sorulacak ve cevaplarınıza göre otomatik wordlist oluşturulacaktır!

🔐 Güvenlik & Yasal Uyarı (Security & Disclaimer)
🚨 Bu yazılım sadece eğitim ve araştırma amaçlıdır. Herhangi bir yasa dışı faaliyette kullanılamaz!
🚨 Oluşturulan wordlist dosyalarının kullanımı tamamen kullanıcının sorumluluğundadır.
🚨 Geliştirici hiçbir yasal sorumluluk kabul etmez.

💀 Eğer yasal olmayan bir şey için kullanmayı planlıyorsan, bu programı çalıştırma! 💀

💻 Geliştirici (Developer)
🛠 GitHub: @pixsel9dev
📢 Öneri & Hata Bildirimi: Yeni özellikler için GitHub üzerinden issue açabilirsiniz!

🔥Wordlist ile en güçlü listeleri oluşturun! 🚀😎

