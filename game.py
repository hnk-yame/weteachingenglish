# 5. Sınıf 1. Ünite İngilizce Kelimeleri
WORDS = [
    # Family (Aile)
    "mother", "father", "sister", "brother", "grandmother", "grandfather",
    # Numbers (Sayılar)
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    # Colors (Renkler)
    "red", "blue", "yellow", "green", "black", "white", "orange", "purple",
    # School (Okul)
    "teacher", "student", "book", "pen", "pencil", "desk", "chair", "classroom",
    # Animals (Hayvanlar)
    "cat", "dog", "bird", "fish", "rabbit", "elephant", "lion", "tiger",
]

import random

class Game:
    def __init__(self):
        self.rooms = {}
        self.word_list = WORDS
    
    def create_room(self, room_code):
        """Oda oluştur"""
        if room_code not in self.rooms:
            self.rooms[room_code] = {
                "players": {},
                "current_round": 0,
                "words": [],
                "game_started": False
            }
            return True
        return False
    
    def join_room(self, room_code, player_name):
        """Oyuncuyu odaya katıl"""
        if room_code in self.rooms and len(self.rooms[room_code]["players"]) < 2:
            self.rooms[room_code]["players"][player_name] = {
                "score": 0,
                "current_word_index": 0,
                "correct_answers": 0
            }
            return True
        return False
    
    def start_game(self, room_code):
        """Oyunu başlat"""
        if room_code in self.rooms and len(self.rooms[room_code]["players"]) == 2:
            self.rooms[room_code]["game_started"] = True
            self.rooms[room_code]["words"] = random.sample(self.word_list, 4)
            return True
        return False
    
    def check_answer(self, room_code, player_name, word, answer):
        """Cevabı kontrol et"""
        if word.lower() == answer.lower():
            self.rooms[room_code]["players"][player_name]["score"] += 10
            self.rooms[room_code]["players"][player_name]["correct_answers"] += 1
            return True
        else:
            # Yanlış yazınca 2 puan kaybı
            self.rooms[room_code]["players"][player_name]["score"] -= 2
            if self.rooms[room_code]["players"][player_name]["score"] < 0:
                self.rooms[room_code]["players"][player_name]["score"] = 0
            return False
    
    def get_room_status(self, room_code):
        """Oda durumunu döndür"""
        if room_code in self.rooms:
            return self.rooms[room_code]
        return None
