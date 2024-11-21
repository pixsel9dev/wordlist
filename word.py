import argparse
from itertools import product

def generate_wordlist(data, output, min_len, max_len):
    print("\n--- Wordlist Oluşturuluyor... ---\n")
    
    with open(output, "w", encoding="utf-8") as file:
        for length in range(min_len, max_len + 1):
            for combo in product(data, repeat=length):
                word = "".join(combo)
                file.write(word + "\n")
                print(f"Oluşturuldu: {word}")
    
    print(f"\nWordlist başarıyla {output} dosyasına kaydedildi!")

def interactive_mode():
    print("\n--- Etkileşimli Wordlist Oluşturucu ---")
    print("Detaylı soruları yanıtlayarak devasa bir wordlist oluşturun.\n")
    
    names = input("İsimler (Boşlukla ayrılmış şekilde yazın, örnek: Ali Ayşe Mehmet): ").split()
    surnames = input("Soyisimler (Boşlukla ayrılmış şekilde yazın, örnek: Yılmaz Demir Aksoy): ").split()
    birthdays = input("Doğum tarihleri veya özel tarih formatları (örnek: 1990 2000 01011990): ").split()
    keywords = input("Özel kelimeler veya anahtar kelimeler (örnek: password hacker admin): ").split()
    numbers = input("Özel sayılar (örnek: 123 456 789): ").split()
    special_chars = input("Özel karakterler (örnek: @ # $ % &): ").split()
    custom_words = input("Kendi belirlediğiniz diğer kelimeler (örnek: araba ev hayal): ").split()
    min_len = int(input("Kombinasyonların minimum uzunluğu (örnek: 2): "))
    max_len = int(input("Kombinasyonların maksimum uzunluğu (örnek: 5): "))
    output = input("Wordlist'in kaydedileceği dosya adı (örnek: wordlist.txt): ")
    
    all_inputs = names + surnames + birthdays + keywords + numbers + special_chars + custom_words
    generate_wordlist(all_inputs, output, min_len, max_len)

def main():
    print("\n--- Wordlist Oluşturucu ---")
    print("Bu program çok detaylı sorular sorarak devasa bir wordlist oluşturur.")
    
    parser = argparse.ArgumentParser(
        description="Dünyanın en iyi wordlist oluşturma programı. Kullanıcıdan detaylı veriler alarak tek dosyada devasa bir wordlist oluşturur."
    )
    
    parser.add_argument(
        "-n", "--names",
        type=str,
        nargs="+",
        help="İsimler (Boşlukla ayrılmış şekilde yazın, örnek: Ali Ayşe Mehmet)"
    )
    
    parser.add_argument(
        "-sn", "--surnames",
        type=str,
        nargs="+",
        help="Soyisimler (Boşlukla ayrılmış şekilde yazın, örnek: Yılmaz Demir Aksoy)"
    )
    
    parser.add_argument(
        "-b", "--birthdays",
        type=str,
        nargs="+",
        help="Doğum tarihleri veya özel tarih formatları (örnek: 1990 2000 01011990)"
    )
    
    parser.add_argument(
        "-k", "--keywords",
        type=str,
        nargs="+",
        help="Özel kelimeler veya anahtar kelimeler (örnek: password hacker admin)"
    )
    
    parser.add_argument(
        "-nu", "--numbers",
        type=str,
        nargs="+",
        help="Özel sayılar (örnek: 123 456 789)"
    )
    
    parser.add_argument(
        "-s", "--special_chars",
        type=str,
        nargs="+",
        help="Özel karakterler (örnek: @ # $ %% &)"
    )
    
    parser.add_argument(
        "-cw", "--custom_words",
        type=str,
        nargs="+",
        help="Kendi belirlediğiniz diğer kelimeler (örnek: araba ev hayal)"
    )
    
    parser.add_argument(
        "-min", "--min_len",
        type=int,
        help="Kombinasyonların minimum uzunluğu (örnek: 2)"
    )
    
    parser.add_argument(
        "-max", "--max_len",
        type=int,
        help="Kombinasyonların maksimum uzunluğu (örnek: 5)"
    )
    
    parser.add_argument(
        "-o", "--output",
        type=str,
        help="Wordlist'in kaydedileceği dosya adı (örnek: wordlist.txt)"
    )
    
    parser.add_argument(
        "-e", "--interactive",
        action="store_true",
        help="Etkileşimli modu etkinleştir (Soruları terminalden yanıtlayarak oluşturun)."
    )
    
    args = parser.parse_args()
    
    if args.interactive:
        interactive_mode()
    else:
        all_inputs = (
            (args.names or []) +
            (args.surnames or []) +
            (args.birthdays or []) +
            (args.keywords or []) +
            (args.numbers or []) +
            (args.special_chars or []) +
            (args.custom_words or [])
        )
        if not all_inputs or not args.min_len or not args.max_len or not args.output:
            print("Tüm parametreler belirtilmelidir. Daha fazla bilgi için -h kullanın.")
            return
        
        generate_wordlist(all_inputs, args.output, args.min_len, args.max_len)

if __name__ == "__main__":
    main()
