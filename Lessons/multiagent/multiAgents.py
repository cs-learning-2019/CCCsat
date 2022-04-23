# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"
        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        score = successorGameState.getScore()
        return score

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        best_move = self.DFMiniMax(self.depth + 1, self.index, gameState)
        return best_move[0]

    def DFMiniMax(self, depth, index, game_state):
        if index == 0:  # we only need to decrement the depth when we get to Pacman's turn
            depth -= 1
        best_move = "Stop"  # Default value

        # Check to see if we are at a leaf in the game tree
        if depth == 0 or game_state.isWin() or game_state.isLose():
            return (best_move, self.evaluationFunction(game_state))

        # We are not at a leaf so check who is suppose to go
        if index == 0:  # Pacman = Max player
            value = -10000000
        else:  # Otherwise it must be ghost = Min player
            value = 10000000

        # Expand the tree from the current node
        for move in game_state.getLegalActions(index):
            next_game_state = game_state.generateSuccessor(index, move)
            if index == game_state.getNumAgents() - 1:
                next_index = 0
            else:
                next_index = index + 1
            sub_best_move = self.DFMiniMax(depth, next_index, next_game_state)
            if index == 0 and value < sub_best_move[1]:
                value = sub_best_move[1]
                best_move = move
            if (not (index ==  0)) and value > sub_best_move[1]:
                value = sub_best_move[1]
                best_move = move

        return (best_move, value)

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        best_move = self.Alpha_Beta(self.depth + 1, self.index, -10000000, 10000000, gameState)
        return best_move[0]

    def Alpha_Beta(self, depth, index, alpha, beta, game_state):
        "*** YOUR CODE HERE ***"
        if index == 0:  # we only need to decrement the depth when we get to Pacman's turn
            depth -= 1
        best_move = "Stop"  # Default value

        # Check to see if we are at a leaf in the game tree
        if depth == 0 or game_state.isWin() or game_state.isLose():
            return (best_move, self.evaluationFunction(game_state))

        # We are not at a leaf so check who is suppose to go
        if index == 0:  # Pacman = Max player
            value = -10000000
        else:  # Otherwise it must be ghost = Min player
            value = 10000000

        # Expand the tree from the current node
        for move in game_state.getLegalActions(index):
            next_game_state = game_state.generateSuccessor(index, move)
            if index == game_state.getNumAgents() - 1:
                next_index = 0
            else:
                next_index = index + 1
            sub_best_move = self.Alpha_Beta(depth, next_index, alpha, beta, next_game_state)
            if index == 0:
                if value < sub_best_move[1]:
                    value = sub_best_move[1]
                    best_move = move
                if value >= beta:
                    return (best_move, value)
                alpha = max(alpha, value)
            if (not (index ==  0)):
                if value > sub_best_move[1]:
                    value = sub_best_move[1]
                    best_move = move
                if value <= alpha:
                    return (best_move, value)
                beta = min(beta, value)

        return (best_move, value)


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        best_move = self.Expectimax(self.depth + 1, self.index, gameState)
        return best_move[0]

    def Expectimax(self, depth, index, game_state):
        "*** YOUR CODE HERE ***"
        if index == 0:  # we only need to decrement the depth when we get to Pacman's turn
            depth -= 1
        best_move = "Stop"  # Default value

        # Check to see if we are at a leaf in the game tree
        if depth == 0 or game_state.isWin() or game_state.isLose():
            return (best_move, self.evaluationFunction(game_state))

        # We are not at a leaf so check who is suppose to go
        if index == 0:  # Pacman = Max player
            value = -10000000
        else:  # Otherwise it must be ghost = Chance player
            value = 0

        # Expand the tree from the current node
        for move in game_state.getLegalActions(index):
            next_game_state = game_state.generateSuccessor(index, move)
            if index == game_state.getNumAgents() - 1:
                next_index = 0
            else:
                next_index = index + 1
            sub_best_move = self.Expectimax(depth, next_index, next_game_state)
            if index == 0 and value < sub_best_move[1]:
                value = sub_best_move[1]
                best_move = move
            if (not (index == 0)):
                value += sub_best_move[1] * (1.0 / float(len(game_state.getLegalActions(index))))
                best_move = move

        return (best_move, value)

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
            This evaluation function is similar to the one I had for question 1. The only
            difference is now we are looking at the current game state as opposed to the
            game state after a certain action. This function takes into account the closest
            food and the manhattan distance to it. The smaller the distance to the closest
            food the better the game state. This is captured by taking the reciprocal with
            an addition factor of 10. I found that 10 worked nicely (by trial and error).
            Next I considered the ghosts positions and the closer Pacman is to each ghost
            the more I deducted score. Again I used the factor of 10 since it worked well.
            I also included an if statement to add to the score if Pacman was close to a
            scared ghost so that Pacman would be encourage to eat the ghost. Finally, there
            is an if statement to check if Pacman is dangerously close to a ghost and if so
            I greatly reduce the score of the state in hopes that Pacman will move away from
            the ghost otherwise Pacman will most likely die.
    """
    "*** YOUR CODE HERE ***"
    # Useful information you can extract from a GameState (pacman.py)
    newPos = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood()
    newGhostStates = currentGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

    "*** YOUR CODE HERE ***"
    score = currentGameState.getScore()

    # First lets look at the remaining foods and their distance to Pacman
    closest_food_dist = 100000
    for food_pos in newFood.asList():
        if (currentGameState.hasFood(food_pos[0], food_pos[1])):
            temp = util.manhattanDistance(food_pos, newPos)
            closest_food_dist = min(closest_food_dist, temp)
    score += 10 / closest_food_dist

    # Now lets look at the position of the ghost(s) relative to Pacman
    all_ghost_pos = currentGameState.getGhostPositions()
    index = 0
    for ghost in all_ghost_pos:
        if newScaredTimes[index] > 10:
            score += (400 / util.manhattanDistance(ghost, newPos))
        elif util.manhattanDistance(ghost, newPos) <= 1:
            score -= 100000000  # We must ensure Pacman does not die
        elif util.manhattanDistance(ghost, newPos) > 1:
            score -= 10 / (util.manhattanDistance(ghost, newPos))
        index += 1

    return score

# Abbreviation
better = betterEvaluationFunction

