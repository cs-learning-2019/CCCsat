# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    open_list = util.Stack()
    open_list.push([(problem.getStartState(), "", 0)])

    while not open_list.isEmpty():
        node = open_list.pop()
        end_state = node[len(node) - 1][0]
        if problem.isGoalState(end_state):
            move_list = []
            for step in node:
                move_list.append(step[1])
            move_list.pop(0)
            return move_list
        for succ in problem.getSuccessors(end_state):
            state_pos = succ[0]
            good = True
            for step in node:
                if step[0] == state_pos:
                    good = False
            if good == True:
                open_list.push(node + [succ])

    return []  # No solution path found

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    open_list = util.Queue()
    open_list.push([(problem.getStartState(), "", 0)])
    seen = {problem.getStartState(): 0}

    while not open_list.isEmpty():
        node = open_list.pop()
        end_state = node[len(node) - 1][0]
        move_list = []
        for step in node:
            move_list.append(step[1])
        move_list.pop(0)
        if problem.getCostOfActions(move_list) <= seen[end_state]:
            if problem.isGoalState(end_state):
                return move_list
            for succ in problem.getSuccessors(end_state):
                state_pos = succ[0]
                if (state_pos not in seen) or (problem.getCostOfActions(move_list + [succ[1]]) < seen[state_pos]):
                    open_list.push(node + [succ])
                    seen[state_pos] = problem.getCostOfActions(move_list + [succ[1]])

    return []  # No solution path found

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    open_list = util.PriorityQueue()
    open_list.push([(problem.getStartState(), "", 0)], 0)
    seen = {problem.getStartState(): 0}

    while not open_list.isEmpty():
        node = open_list.pop()
        end_state = node[len(node) - 1][0]
        move_list = []
        for step in node:
            move_list.append(step[1])
        move_list.pop(0)
        if problem.getCostOfActions(move_list) <= seen[end_state]:
            if problem.isGoalState(end_state):
                return move_list
            for succ in problem.getSuccessors(end_state):
                state_pos = succ[0]
                if (state_pos not in seen) or (problem.getCostOfActions(move_list + [succ[1]]) < seen[state_pos]):
                    open_list.push(node + [succ], problem.getCostOfActions(move_list + [succ[1]]))
                    seen[state_pos] = problem.getCostOfActions(move_list + [succ[1]])

    return []  # No solution path found

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    open_list = util.PriorityQueue()
    open_list.push([(problem.getStartState(), "", (0, heuristic(problem.getStartState(), problem)))],
                   0 + heuristic(problem.getStartState(), problem))
    seen = {problem.getStartState(): 0}

    while not open_list.isEmpty():
        node = open_list.pop()

        # tie breaking
        # You need to code this
        # At the end of the tie breaking section your node variable will be set to the node that wins the tie break
        # Note: if there was no tie then node does not change

        move_list = [step[1] for step in node]
        move_list.pop(0)
        end_state = node[len(node) - 1][0]
        if problem.getCostOfActions(move_list) <= seen[end_state]:
            if problem.isGoalState(end_state):
                return move_list
            for succ in problem.getSuccessors(end_state):
                state_pos = succ[0]
                temp = (problem.getCostOfActions(move_list) + succ[2], heuristic(state_pos, problem))
                succ = (succ[0], succ[1], temp)
                if (state_pos not in seen) or (problem.getCostOfActions(move_list + [succ[1]]) < seen[state_pos]):
                    open_list.push(node + [succ],
                                   problem.getCostOfActions(move_list + [succ[1]]) + heuristic(state_pos, problem))
                    seen[state_pos] = problem.getCostOfActions(move_list + [succ[1]])

    return []  # No solution path found


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
