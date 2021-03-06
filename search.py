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

    """

    # print ("Start: {}".format(problem.getStartState()))
    # print ("Is the start a goal? {}".format(problem.isGoalState(problem.getStartState())))
    # print ("Start's successors: {}".format(problem.getSuccessors(problem.getStartState())))

    curr_state = problem.getStartState()
    frontiers = util.Stack()
    frontiers.push(curr_state)

    node_dict = {curr_state: (None, None)}  # dict of node to (prev node, dir, depth)
    explored = set()

    while True:
        f = frontiers.pop()  # get the next priority node
        explored.add(f)  # add it to explored

        if problem.isGoalState(f): # if we reached goal state, return the path
            path = util.Stack()
            node = f
            while node_dict[node][1] is not None:
                path.push(node_dict[node][1])
                node = node_dict[node][0]
            path_list = []
            while not path.isEmpty():
                path_list.append(path.pop())
            return path_list

        next_cand = [n for n in problem.getSuccessors(f) if (n[0] not in explored) and (n[0] not in frontiers.list)]

        if len(next_cand) == 0:
            if frontiers.isEmpty():
                raise Exception("there is no goal state")
            else:
                continue

        for n in next_cand:
            node = n[0]
            dir = n[1]

            node_dict[node] = (f, dir)
            frontiers.push(node)

    raise NotImplementedError


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    curr_state = problem.getStartState()
    frontiers = util.Queue()
    frontiers.push(curr_state)

    node_dict = {curr_state: (None, None, 0)}  # dict of node to (prev node, dir, depth)
    explored = set()

    while True:
        f = frontiers.pop()  # get the next priority nodes
        explored.add(f)  # add it to explored

        if problem.isGoalState(f): # if we reached goal state, return the path
            path = util.Stack()
            node = f
            while node_dict[node][1] is not None:
                path.push(node_dict[node][1])
                node = node_dict[node][0]
            path_list = []
            while not path.isEmpty():
                path_list.append(path.pop())
            return path_list

        next_cand = [n for n in problem.getSuccessors(f) if (n[0] not in explored) and (n[0] not in frontiers.list)]

        if len(next_cand) == 0:
            if frontiers.isEmpty():
                raise Exception("there is no goal state")
            else:
                continue

        for n in next_cand:
            node = n[0]
            dir = n[1]

            node_dict[node] = (f, dir)
            # print("add frontier node {} dir {} depth {}".format(node, node_dict[node][1], node_dict[node][2]))
            frontiers.push(node)
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
