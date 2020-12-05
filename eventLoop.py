import constants as c
import state
import ui

# While the state doesn't tell us to quit...
while state.gameState != c.QUIT:

  # STANDBY then switch to GET_SECRET
  if state.gameState == c.STANDBY:
    state = state.setGameState(state, c.GET_SECRET)

  # GET_SECRET then switch to GET_GUESS
  elif state.gameState == c.GET_SECRET:
    newSecret = ui.getNewSecret()
    newSecret = ui.validateInput(newSecret)
    if newSecret == False:
      print("Use the numbers that correspond to the colors you want. Your pattern must have exactly four numbers")
    else:
      state = state.setGameState(state, c.GET_GUESS)

  # GET_GUESS -> validate guess and save
  elif state.gameState == c.GET_GUESS:
    newGuess = ui.getNewGuess()
    newGuess = ui.validateInput(newGuess)
    if newGuess == False:
      print("Use the numbers that correspond to the colors you want. Your pattern must have exactly four numbers")
    else:
      ui.printGuess(state)
      state = state.setGuess(state, newGuess)

  # COMPUTE_FEEDBACK -> analyze guess / offer feedback
  elif state.gameState == c.COMPUTE_FEEDBACK:
      if (isGuessCorrect(state)):
        state = state.addScore(state)
        state = state.switchPlayer(state)
        state = state.setGameState(state, c.GET_SECRET)
        ui.printWinMessage(state)
        ui.printScore(state)
      else:
        state = state.setFeedback(state)
        state = state.addGuessCount(state)
        ui.printFeedback(state)

ui.printScore(state)
exit(0)
