# app.py
from flask import Flask, render_template, request, jsonify
from othello_game import OthelloGame

app = Flask(__name__)
game = OthelloGame()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_board', methods=['GET'])
def get_board():
    return jsonify(game.get_board())

@app.route('/make_move', methods=['POST'])
def make_move():
    data = request.get_json()
    row, col = data['row'], data['col']
    game.make_move(row, col)
    return jsonify({"status": "success", "current_player": game.current_player})

if __name__ == '__main__':
    app.run(debug=True)
