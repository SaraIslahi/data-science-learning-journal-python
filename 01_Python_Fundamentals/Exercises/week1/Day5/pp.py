import os
import sys # sys is sometimes needed for console output handling

# --- Configuration ---
BOARD_SIZE = 3
EMPTY_CELL = ' '
def create_board():
    """Initializes and returns an empty 3x3 Tic-Tac-Toe board."""
    return [[EMPTY_CELL for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
def display_board(board):
    """Prints the current state of the board in a visually clear 3x3 grid format."""
    
    # 1. Column Header (Aligned with cells: 0 | 1 | 2)
    header_numbers = " | ".join(str(i) for i in range(BOARD_SIZE))
    print("\n    " + header_numbers)
    
    # Determine the length of the separator line for alignment
    SEPARATOR_LENGTH = BOARD_SIZE * 4 + 1 
    
    # 2. Print Separator Line
    print("  " + "-" * SEPARATOR_LENGTH) 
    
    # 3. Print Rows
    for i, row in enumerate(board):
        # Print the row content (e.g., 0 | X |   | O |)
        print(f"{i} | {' | '.join(row)} |")
        # Print the separator line after the row
        print("  " + "-" * SEPARATOR_LENGTH)

    print() # Final newline for spacing

    a=create_board()
    print(a)