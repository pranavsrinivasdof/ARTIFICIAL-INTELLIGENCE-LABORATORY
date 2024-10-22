class PuzzleState:
    def __init__(self, board, empty_tile_pos, path=[]):
        self.board = board
        self.empty_tile_pos = empty_tile_pos
        self.path = path

    def is_goal(self):
        return self.board == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def get_possible_moves(self):
        moves = []
        row, col = self.empty_tile_pos
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_board = self.board[:]
                # Swap the empty tile with the adjacent tile
                new_board[row * 3 + col], new_board[new_row * 3 + new_col] = new_board[new_row * 3 + new_col], new_board[row * 3 + col]
                moves.append((new_board, (new_row, new_col)))

        return moves

def dfs(state, visited):
    if state.is_goal():
        return state.path

    visited.add(tuple(state.board))  # Mark the state as visited

    for new_board, new_empty_pos in state.get_possible_moves():
        if tuple(new_board) not in visited:
            new_state = PuzzleState(new_board, new_empty_pos, state.path + [new_board])
            result = dfs(new_state, visited)
            if result is not None:
                return result

    return None  # No solution found

def display_board(board):
    for i in range(3):
        print(board[i*3:(i+1)*3])  # Print each row

# Example usage
initial_board = [1, 2, 3, 4, 5, 6, 0, 7, 8]  # 0 represents the empty tile
initial_empty_pos = (2, 0)  # The position of the empty tile (row, col)
initial_state = PuzzleState(initial_board, initial_empty_pos)

visited = set()
solution = dfs(initial_state, visited)

if solution:
    print("Solution found:")
    for step in solution:
        display_board(step)
        print()  # Blank line between steps
else:
    print("No solution found.")
