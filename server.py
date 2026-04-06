from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room
from game import Game

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")
game = Game()

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>We Teaching English - Oyun</title>
        <style>
            body { font-family: Arial; text-align: center; margin: 50px; }
            .container { max-width: 600px; margin: 0 auto; }
            input, button { padding: 10px; margin: 5px; font-size: 16px; }
            button { background-color: #4CAF50; color: white; border: none; cursor: pointer; }
            button:hover { background-color: #45a049; }
            .game-area { border: 2px solid #333; padding: 20px; margin: 20px 0; }
            .score { font-size: 20px; font-weight: bold; }
            .word { font-size: 32px; color: #2196F3; margin: 20px 0; }
        </style>
        <script src="https://cdn.socket.io/4.5.4/socket.io.min.js"></script>
    </head>
    <body>
        <div class="container">
            <h1>🎮 We Teaching English - Kelime Yarışması</h1>
            
            <div id="login-area">
                <input type="text" id="playerName" placeholder="Oyuncu adını gir">
                <input type="text" id="roomCode" placeholder="Oda kodu (ör: ABC123)">
                <button onclick="createRoom()">Oda Oluştur</button>
                <button onclick="joinRoom()">Odaya Katıl</button>
            </div>
            
            <div id="game-area" style="display:none;" class="game-area">
                <div class="score">Skorun: <span id="score">0</span></div>
                <div class="score">Rakip Skoru: <span id="opponent-score">0</span></div>
                
                <h2 id="round-info">Hazırlanıyor...</h2>
                
                <div class="word" id="word">Bekleniyor...</div>
                
                <input type="text" id="answer" placeholder="Kelimeyi yazın..." disabled>
                <button onclick="submitAnswer()" id="submit-btn" disabled>Gönder</button>
                
                <div id="message" style="margin-top: 10px; font-size: 18px;"></div>
            </div>
        </div>

        <script>
            const socket = io();
            let playerName = '';
            let roomCode = '';
            let currentWord = '';
            let wordIndex = 0;

            function createRoom() {
                playerName = document.getElementById('playerName').value;
                roomCode = document.getElementById('roomCode').value;
                
                if (!playerName || !roomCode) {
                    alert('Lütfen ad ve oda kodunu gir!');
                    return;
                }
                
                socket.emit('create_room', {room_code: roomCode, player_name: playerName});
            }

            function joinRoom() {
                playerName = document.getElementById('playerName').value;
                roomCode = document.getElementById('roomCode').value;
                
                if (!playerName || !roomCode) {
                    alert('Lütfen ad ve oda kodunu gir!');
                    return;
                }
                
                socket.emit('join_room', {room_code: roomCode, player_name: playerName});
            }

            function submitAnswer() {
                const answer = document.getElementById('answer').value;
                if (answer.trim()) {
                    socket.emit('submit_answer', {
                        room_code: roomCode,
                        player_name: playerName,
                        word: currentWord,
                        answer: answer
                    });
                    document.getElementById('answer').value = '';
                }
            }

            // Socket olayları
            socket.on('room_created', (data) => {
                alert('Oda oluşturuldu! Kodu: ' + roomCode);
                socket.emit('start_game', {room_code: roomCode});
            });

            socket.on('room_joined', (data) => {
                alert('Odaya katıldın! Oyun başlıyor...');
                document.getElementById('login-area').style.display = 'none';
                document.getElementById('game-area').style.display = 'block';
                socket.emit('start_game', {room_code: roomCode});
            });

            socket.on('game_started', (data) => {
                document.getElementById('login-area').style.display = 'none';
                document.getElementById('game-area').style.display = 'block';
                nextWord(data);
            });

            socket.on('next_word', (data) => {
                nextWord(data);
            });

            function nextWord(data) {
                if (wordIndex < 4) {
                    currentWord = data.words[wordIndex];
                    document.getElementById('word').textContent = currentWord;
                    document.getElementById('round-info').textContent = `Tur ${wordIndex + 1}/4`;
                    document.getElementById('answer').disabled = false;
                    document.getElementById('submit-btn').disabled = false;
                    document.getElementById('message').textContent = '';
                } else {
                    gameEnd(data);
                }
            }

            socket.on('answer_result', (data) => {
                document.getElementById('score').textContent = data.player_score;
                document.getElementById('opponent-score').textContent = data.opponent_score;
                
                if (data.correct) {
                    document.getElementById('message').textContent = '✅ Doğru!';
                } else {
                    document.getElementById('message').textContent = '❌ Yanlış! -2 puan';
                }
                
                setTimeout(() => {
                    wordIndex++;
                    if (wordIndex < 4) {
                        socket.emit('get_next_word', {room_code: roomCode});
                    } else {
                        gameEnd(data);
                    }
                }, 1500);
            });

            function gameEnd(data) {
                document.getElementById('game-area').style.display = 'none';
                alert('Oyun bitti! Senin puanın: ' + data.player_score + ' | Rakip: ' + data.opponent_score);
            }
        </script>
    </body>
    </html>
    '''

@socketio.on('create_room')
def handle_create_room(data):
    room_code = data['room_code']
    player_name = data['player_name']
    
    if game.create_room(room_code):
        if game.join_room(room_code, player_name):
            emit('room_created', {'message': 'Oda oluşturuldu'})
    else:
        emit('error', {'message': 'Oda zaten var!'})

@socketio.on('join_room')
def handle_join_room(data):
    room_code = data['room_code']
    player_name = data['player_name']
    
    if game.join_room(room_code, player_name):
        join_room(room_code)
        emit('room_joined', {'message': 'Odaya katıldın'}, room=room_code)
    else:
        emit('error', {'message': 'Odaya katılamadın!'})

@socketio.on('start_game')
def handle_start_game(data):
    room_code = data['room_code']
    if game.start_game(room_code):
        room_status = game.get_room_status(room_code)
        emit('game_started', {'words': room_status['words']}, room=room_code)

@socketio.on('submit_answer')
def handle_submit_answer(data):
    room_code = data['room_code']
    player_name = data['player_name']
    word = data['word']
    answer = data['answer']
    
    correct = game.check_answer(room_code, player_name, word, answer)
    room_status = game.get_room_status(room_code)
    
    players = list(room_status['players'].keys())
    opponent_name = players[0] if players[1] == player_name else players[1]
    
    emit('answer_result', {
        'correct': correct,
        'player_score': room_status['players'][player_name]['score'],
        'opponent_score': room_status['players'][opponent_name]['score'],
        'words': room_status['words']
    }, room=room_code)

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
