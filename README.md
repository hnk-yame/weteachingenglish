import random

# 5. sınıf 1. ünite kelimeleri ve anlamlari (örnektir)
kelimeler = {
    "book": "kitap",
    "school": "okul",
    "teacher": "öğretmen",
    "friend": "arkadaş",
    "headmaster":"okul müdürü",
    "student":"öğrenci",
    "asistant":"asistan",
    "coach": "koç",
    "canteeen":"kantin",
    "classroom":"sınıf",
    "gate":"kapı",
    "lab":"laboratuvar",
    "libary":"kütüphane",
    "playground":"oyun alanı",
    "sports field":"spor sahası",
    "arrange":"düzenlemek",
    "organize":"düzenlemek",
    "art club":"sanat kulübü",
    "chess club":"satranç kulübü",
    "film club": "film kulübü",
    "folk dance club":"hal oyunları kulübü",
    "maths club":"matematik kulübü",
    "music club":"müzik kulübü",
    "science club":"bilim kulübü",
    "technology club":"teknoloji kulübü",
    "answer":"cevaplamak",
    "ask":"sormak",
    "celebrate":"kutlamak",
    "choose":"seçmek",
    "correct":"doğru",
    "do":"yapmak",
    "find":"bulmak",
    "join":"katılmak",
    "look":"bakmak",
    "like":"beğenmek",
    "run":"koşmak",
    "shout":"bağırmak",
    "say":"söylemek",
    "see":"görmek",
    "talk":"konuşmak",
    "love":"sevmek",
    "safe":"güvenli",
    "kind":"nazik",
    "nice":"güzel",
    "different":"farklı"
}

score = 0  # Başlangıç puanı

def kelime_quiz():
    global score
    kelime, anlam = random.choice(list(kelimeler.items()))
    cevap = input(f"Bu kelimenin Türkçesi nedir? '{kelime}': ").lower()
    if cevap == anlam:
        print("Tebrikler! Doğru cevap.")
        score += 10
    else:
        print(f"Yanlış cevap. Doğru cevap: {anlam}")
    print(f"Güncel puanınız: {score}")

def kelime_listesi_göster():
    print("Kelime listesi:")
    for k, a in kelimeler.items():
        print(f"- {k}: {a}")

# Kullanici secimi
while True:
    print("\nSecenekler:")
    print("1 - Kelime quiz")
    print("2 - Kelime listesi göster")
    print("3 - Çıkış")
    secim = input("Seçiminizi girin (1/2/3): ")

    if secim == "1":
        kelime_quiz()
    elif secim == "2":
        kelime_listesi_göster()
    elif secim == "3":
        print(f"Programdan cikiliyor... Toplam puaniniz: {score}")
        break
    else:
        print("Geçersiz seçim. Tekrar deneyin.")
