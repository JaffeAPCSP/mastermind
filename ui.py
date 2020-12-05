def getStringFromKeyboard(message):
  return input(message)

def printScore(state):
  print("Player 1 score: "+state.score1)
  print("Player 2 score: "+state.score2)

def printWinMessage(state):
  print("Player "+str(state.player)+" guessed the pattern!")

def printGuess(state):
  print("Current guess: "+state.guess)

def printSecret(state):
  print("Secret code: "+state.secret)

def printFeedback(state):
  print("Feedback: "+state.feedback)

def validateSecret(code):
  try:
    code = int(str)      # convert to integer
    return code
  except:
    return False         # conversion error

def validateGuess(secret, code):
  isNumber = validateSecret(code)
  if not isNumber:
    return code
  else:
    return False
