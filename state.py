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

def setGameState(state, newGameState):
  state.gameState = newGameState;
  return state

def addGuessCount(state):
  state.guessCount = state.guessCount + 1
  return state

def addScoreToCurrentPlayer(state):
  if state.player == 1:
    state.score2 += state.guessCount
  else:
    state.score1 += state.guessCount
  return state

def switchPlayer(state):
  if state.player == 1:
    state.player = 2
  else:
    state.player = 1
  return state

def computeAndSetFeedback(state):
  secretList = list(state.secret) # convert to list
  guessList = list(state.guess)   # convert to list
  usedList = [False for i in range(len(secretList))]
  feedbackList = ['' for i in range(len(secretList))]

  for index in range(len(secretList)):
    if secretList[index] == guessList[index]:
      feedbackList[index] = guessList[index]
      usedList[index] = True

  for guessIndex in range(len(guessList)):
    if not guessList[guessIndex]:
      for secretIndex in range(len(secretList)):
        if guessList[guessIndex] == secretList[secretIndex] and not usedList[secretIndex]:
          feedbackList[guessIndex] = c.PRESENT
          usedList[secretIndex] = True
          # break out of inner loop, goto next guess letter
          break

  for feedbackIndex in range(len(feedbackList)):
    if not usedList[feedbackIndex]:
      feedbackList[feedbackIndex] = c.NOT_PRESENT

  state.feedback = "".join(feedbackList)
  return state

