import constants as c
import state
import ui

def isGuessCorrect(state):
  return state.secret == state.guess

# While the state doesn't tell us to quit...
while state.gameState != c.QUIT:

  # STANDBY then switch to GET_SECRET
  if state.gameState == c.STANDBY:
    state = state.setGameState(state, c.GET_SECRET)

  # GET_SECRET then switch to GET_GUESS
  elif state.gameState == c.GET_SECRET:
    newSecret = ui.getStringFromKeyboard("Enter the new secret code using digits 0-9")
    newSecret = ui.validateSecret(newSecret)
    if newSecret == False:
      print("Your secret code must only contain digits 0 through 9")
    else:
      state = state.setGameState(state, c.GET_GUESS)

  # GET_GUESS -> validate guess and save
  elif state.gameState == c.GET_GUESS:
    newGuess = ui.getStringFromKeyboard("Enter your guess of "+len(state.secret)+" digits 0-9")
    newGuess = ui.validateGuess(state.secret, newGuess)
    if newGuess == False:
      print("Your secret code must only contain digits 0 through 9")
    else:
      ui.printGuess(state)
      state = state.setGuess(state, newGuess)

  # COMPUTE_FEEDBACK -> analyze guess / offer feedback
  elif state.gameState == c.COMPUTE_FEEDBACK:
      if (isGuessCorrect(state)):
        state = state.addScoreToCurrentPlayer(state)
        state = state.switchPlayer(state)
        state = state.setGameState(state, c.GET_SECRET)
        ui.printWinMessage(state)
        ui.printScore(state)
      else:
        state = state.computeAndSetFeedback(state)
        state = state.addGuessCount(state)
        ui.printFeedback(state)

ui.printScore(state)
exit(0)
