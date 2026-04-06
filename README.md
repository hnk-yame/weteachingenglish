import random

kelimeler = {
    "book": "kitap",
    "school": "okul",
    "teacher": "öğretmen",
    "friend": "arkadaş",
    "headmaster": "okul müdürü",
    "student": "öğrenci",
    "assistant": "asistan",
    "coach": "koç",
    "canteen": "kantin",
    "classroom": "sınıf",
    "gate": "kapı",
    "lab": "laboratuvar",
    "library": "kütüphane",
    "playground": "oyun alanı",
    "sports field": "spor sahası",
    "arrange": "düzenlemek",
    "organize": "düzenlemek",
    "art club": "sanat kulübü",
    "chess club": "satranç kulübü",
    "film club": "film kulübü",
    "folk dance club": "halk oyunları kulübü",
    "maths club": "matematik kulübü",
    "music club": "müzik kulübü",
    "science club": "bilim kulübü",
    "technology club": "teknoloji kulübü",
    "answer": "cevaplamak",
    "ask": "sormak",
    "celebrate": "kutlamak",
    "choose": "seçmek",
    "correct": "doğru",
    "do": "yapmak",
    "find": "bulmak",
    "join": "katılmak",
    "look": "bakmak",
    "like": "beğenmek",
    "run": "koşmak",
    "shout": "bağırmak",
    "say": "söylemek",
    "see": "görmek",
    "talk": "konuşmak",
    "love": "sevmek",
    "safe": "güvenli",
    "kind": "nazik",
    "nice": "güzel",
    "different": "farklı"
}

score = 0
dogru = 0
yanlis = 0


def coktan_secmeli_quiz():
    global score, dogru, yanlis

    kelime, anlam = random.choice(list(kelimeler.items()))

    # Yanlış şıklar üret
    yanlis_siklar = random.sample(list(kelimeler.values()), 3)
    if anlam in yanlis_siklar:
        yanlis_siklar.remove(anlam)

    secenekler = yanlis_siklar + [anlam]
    random.shuffle(secenekler)

    print(f"\n'{kelime}' kelimesinin Türkçesi nedir?")

    for i, secenek in enumerate(secenekler):
        print(f"{i + 1}) {secenek}")

    cevap = input("Cevabınızı girin (1-4): ")

    if secenekler[int(cevap) - 1] == anlam:
        print("✅ Doğru!")
        score += 10
        dogru += 1
    else:
        print(f"❌ Yanlış! Doğru cevap: {anlam}")
        yanlis += 1

    print(f"Puan: {score} | Doğru: {dogru} | Yanlış: {yanlis}")


def ters_quiz():
    global score

    kelime, anlam = random.choice(list(kelimeler.items()))

    cevap = input(f"\nBu Türkçe kelimenin İngilizcesi nedir? '{anlam}': ").lower()

    if cevap == kelime:
        print("✅ Doğru!")
        score += 10
    else:
        print(f"❌ Yanlış! Doğru cevap: {kelime}")

    print(f"Puan: {score}")


def kelime_listesi_goster():
    print("\nKelime listesi:")
    for k, a in kelimeler.items():
        print(f"- {k}: {a}")


while True:
    print("\n=== MENU ===")
    print("1 - Çoktan seçmeli quiz")
    print("2 - Türkçe → İngilizce quiz")
    print("3 - Kelime listesi")
    print("4 - Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":
        coktan_secmeli_quiz()
    elif secim == "2":
        ters_quiz()
    elif secim == "3":
        kelime_listesi_goster()
    elif secim == "4":
        print(f"Çıkılıyor... Toplam puan: {score}")
        break
    else:
        print("Geçersiz seçim!")
