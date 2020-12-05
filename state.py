import constants as c

gameState = c.STANDBY # Game state
player = 1            # Player with secret 1 or 2
score1 = 0            # Player 1 score
score2 = 0            # Player 2 score
guessCount = 0        # Number of guesses so far
secret = 0            # Secret sequence
guess = 0             # Current guess
feedback = 0          # Feedback information

def setSecret(state, newSecret):
  state.secret = newSecret
  return state

def setGuess(state, newGuess):
  state.guess = newGuess
  return state

def setFeedback(state, newFeedback):
  state.feedback = newFeedback
  return state

def setGameState(state, newGameState):
  state.gameState = newGameState;
  return state

def addGuessCount(state):
  state.guessCount++
  return state

def addScoreToCurrentPlayer(state, scoreToAdd):
  if state.player == 1:
    state.score2 += scoreToAdd
  else:
    state.score1 += scoreToAdd
  return state

def switchPlayer(state):
  if state.player == 1:
    state.player = 2
  else:
    state.player = 1
  return state
