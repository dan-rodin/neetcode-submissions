# R
# Check that no number repeats in any row, column, or 3x3 box.

# T
# Use sets to track numbers already seen in each row, column, and box.

# E
# Loop through every cell. If a value is already in its row, column, or box,
# return False. Otherwise add it to the three sets.

# A
# More generally the space and time is O(n**2) but the board will always be
# a 9x9 = 81 cell board which is a constant so its more like,
# Time: O(1)
# Space: O(1)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(0,9):
            for col in range(0,9):
                val = board[row][col]
                if val == ".":
                    continue
                # can check rows[row],cols[col], but need boxes[box]
                box = (row // 3) * 3 + (col // 3)
                
                if (
                    val in rows[row] or
                    val in cols[col] or
                    val in boxes[box]
                ):
                    return False

                rows[row].add(val)
                cols[col].add(val)
                boxes[box].add(val)
        return True
