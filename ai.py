import random


class AI:
    def choose_column(self, board, me="O", opponent="X"):
        legal = [c for c in range(7) if board.grid[0][c] == "."]

        if not legal:
            return None

        # 1. Take an immediate winning move
        for col in legal:
            row = board.drop(col, me)

            if row is not None:
                won = board.winner(me)
                board.grid[row][col] = "."

                if won:
                    return col

        # 2. Block the opponent's immediate winning move
        for col in legal:
            row = board.drop(col, opponent)

            if row is not None:
                won = board.winner(opponent)
                board.grid[row][col] = "."

                if won:
                    return col

        # 3. Otherwise choose any legal column
        return random.choice(legal)