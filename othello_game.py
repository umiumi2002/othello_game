# othello_game.py
class OthelloGame:
    def __init__(self):
        self.board = [[None] * 8 for _ in range(8)]  # 8x8のボード
        self.current_player = 'B'  # B: 黒, W: 白

    def get_board(self):
        return self.board

    def make_move(self, row, col):
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            self.flip_pieces(row, col)
            self.current_player = 'W' if self.current_player == 'B' else 'B'

    def is_valid_move(self, row, col):
        # ここで、合法手かどうかを判断するロジックを実装します
        return self.board[row][col] is None

    def flip_pieces(self, row, col):
        # ここで、石を裏返すロジックを実装します
        pass
