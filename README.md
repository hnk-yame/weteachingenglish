
import random

words = {
    "anne": "mother",
    "baba": "father",
    "ogretmen": "teacher",
    "kitap": "book",
    "okul": "school",
    "sehir": "city",
    "oyun": "game",
    "muzik": "music",
    "arkadas": "friend",
    "kedi": "cat"
}

print("Ingilizce Kelime Oyununa Hos Geldin!")
print("Turkce kelimenin Ingilizcesini yaz.\n")

score = 0

word_list = list(words.items())
random.shuffle(word_list)

num_questions = min(5, len(word_list))

for i in range(num_questions):
    turkish, english = word_list[i]

    try:
        answer = input(f"{i+1}. '{turkish}' Ingilizcesi nedir? ")
    except EOFError:
        print("\nGirdi alinamadi. Oyun sonlandirildi.")
        break

    answer = answer.strip().lower()

    if answer == "":
        print("Bos cevap girdin!\n")
        continue

    if answer == english:
        print("Dogru!\n")
        score += 1
    else:
        print(f"Yanlis! Dogru cevap: {english}\n")

print(f"Oyun bitti! Skorun: {score}/{num_questions}")
