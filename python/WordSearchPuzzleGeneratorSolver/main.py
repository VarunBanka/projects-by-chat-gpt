import random
import string

# Word search puzzle class
class WordSearch:
  def __init__(self, rows, cols, words):
    self.rows = rows
    self.cols = cols
    self.words = words
    self.grid = [['' for _ in range(cols)] for _ in range(rows)]

  def generate(self):
    # Add words to the grid
    for word in self.words:
      direction = random.choice(['horizontal', 'vertical', 'diagonal'])
      while not self.add_word(word, direction):
        direction = random.choice(['horizontal', 'vertical', 'diagonal'])

    # Add random letters to the empty spots
    self.fill_empty()

    # Return the grid as a list of strings
    return [''.join(row) for row in self.grid]

  def add_word(self, word, direction):
    if direction == 'horizontal':
      return self.add_horizontal(word)
    elif direction == 'vertical':
      return self.add_vertical(word)
    elif direction == 'diagonal':
      return self.add_diagonal(word)

  def add_horizontal(self, word):
    row = random.randint(0, self.rows - 1)
    col = random.randint(0, self.cols - len(word))
    for i, c in enumerate(word):
      if self.grid[row][col + i] and self.grid[row][col + i] != c:
        return False
    for i, c in enumerate(word):
      self.grid[row][col + i] = c
    return True

  def add_vertical(self, word):
    row = random.randint(0, self.rows - len(word))
    col = random.randint(0, self.cols - 1)
    for i, c in enumerate(word):
      if self.grid[row + i][col] and self.grid[row + i][col] != c:
        return False
    for i, c in enumerate(word):
      self.grid[row + i][col] = c
    return True

  def add_diagonal(self, word):
    row = random.randint(0, self.rows - len(word))
    col = random.randint(0, self.cols - len(word))
    for i, c in enumerate(word):
      if self.grid[row + i][col + i] and self.grid[row + i][col + i] != c:
        return False
    for i, c in enumerate(word):
      self.grid[row + i][col + i] = c
    return True

  def fill_empty(self):
    for i in range(self.rows):
      for j in range(self.cols):
        if not self.grid[i][j]:
          self.grid[i][j] = random.choice(string.ascii_lowercase)

# Solver function
def solve(puzzle, words):
  def
