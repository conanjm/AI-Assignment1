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
    """from game import Directions
    path=[Directions.STOP]    
    print "Start:", problem.getStartState()
    if problem.isGoalState(problem.getStartState()) == True
	return path"""
    path={}
    from util import Stack
    nextstates=problem.getSuccessors(problem.getStartState())
    
    fringe=Stack()
    i=0
    parent=problem.getStartState()
    processed=set([parent])
    for state in nextstates:
	if state != problem.getStartState():
	   fringe.push(state)
           path[state]=(parent,'Stop',0)
    while fringe.isEmpty() !=True :
        """print "\n","processed:",processed"""
        state=fringe.pop()
        if state[0] in processed :
           continue
        """ print "\n","processing:",state""" 
        if problem.isGoalState(state[0]) :
            print "\n","goal reached:",state
            i=1
            break
	else :
	    nextstates=problem.getSuccessors(state[0])
            for childstate in nextstates:
               """print "\n","child:",childstate[0]"""
               if childstate[0] not in processed:
                  fringe.push(childstate)
                  path[childstate]=state
                  
            processed.add(state[0])
	    
            """print "\n","searching"""
    if i==0 :
        """print "\n","search failed" """
    else :
        p=[state[1]]
        print p
        pparent=path[state]
        while pparent[0] != parent :
            p.append(pparent[1])
            """print "\n","p:",p"""
            state=pparent
            pparent=path[state]
        """print "\n","p:",p"""
        p.reverse()
        print "\n","p:",p
        return p 

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    path={}
    from util import Queue
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    nextstates=problem.getSuccessors(problem.getStartState())

    fringe=Queue()
    i=0
    parent=problem.getStartState()
    print "\n","start:",parent
    processed=[parent]
    for state in nextstates:
        if state != problem.getStartState():
           fringe.push(state)
           path[state]=(parent,'Stop',0)
    while fringe.isEmpty() !=True :
        state=fringe.pop()
        if state[0] in processed :
           continue
        if problem.isGoalState(state[0]) :
            print "\n","goal reached:",state
            i=1
            break
        else :
            nextstates=problem.getSuccessors(state[0])
            for childstate in nextstates:
               if childstate[0] not in processed:
                  fringe.push(childstate)
                  path[childstate]=state

            processed.append(state[0])

    if i==0 :
        print "\n","search failed"
    else :
        p=[state[1]]
        pparent=path[state]
        while pparent[0] != parent :
            p.append(pparent[1])
            state=pparent
            pparent=path[state]
        p.reverse()
        print "\n","p:",p
        return p

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    path={}
    from util import PriorityQueue
    nextstates=problem.getSuccessors(problem.getStartState())

    fringe=PriorityQueue()
    i=0
    parent=problem.getStartState()
    for state in nextstates:
        if state != problem.getStartState():
           fringe.update(state,problem.getCostOfActions([state[1]]))
           path[state[0]]=[state[1]]
    while fringe.isEmpty() !=True :
        """print "\n","processed:",processed"""
        state=fringe.pop()
        """ print "\n","processing:",state"""
        if problem.isGoalState(state[0]) :
            print "\n","goal reached:",state
            i=1
            break
        else :
            nextstates=problem.getSuccessors(state[0])
            p=path[state[0]]
            for childstate in nextstates :
               p1=p+[childstate[1]]
               cost=problem.getCostOfActions(p1)
               processed=set(path.keys())
               processed.add(parent)
               if childstate[0] not in processed :
                    path[childstate[0]]=p1
                    fringe.update(childstate,cost)
               else :
                    if childstate[0]==parent :
                        prevcost=0
                    else :
                        prevcost=problem.getCostOfActions(path[childstate[0]])
                    if prevcost > cost :
                        del path[childstate[0]]
                        path[childstate[0]]=p1
                        fringe.update(childstate,cost)
                    
                       

            """print "\n","searching"""
    if i==0 :
        print "\n","search failed" 
    else :
        return path[state[0]]

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    path={}
    from util import PriorityQueue
    nextstates=problem.getSuccessors(problem.getStartState())

    fringe=PriorityQueue()
    i=0
    parent=problem.getStartState()
    for state in nextstates:
        if state != problem.getStartState():
           fringe.update(state,problem.getCostOfActions([state[1]])+heuristic(state[0],problem))
           path[state[0]]=[state[1]]
    print path.items()
    print path[state[0]]
    while fringe.isEmpty() !=True :
        """print "\n","processed:",processed"""
        state=fringe.pop()
        """ print "\n","processing:",state"""
        if problem.isGoalState(state[0]) :
            print "\n","goal reached:",state
            i=1
            break
        else :
            nextstates=problem.getSuccessors(state[0])
            p=path[state[0]]
            for childstate in nextstates :
               p1=p+[childstate[1]]
               cost=problem.getCostOfActions(p1)+heuristic(childstate[0],problem)
               processed=set(path.keys())
               processed.add(parent)
               if childstate[0] not in processed :
                    path[childstate[0]]=p1
                    fringe.update(childstate,cost)
               else :
                    if childstate[0]==parent :
                        prevcost=0
                    else :
                        prevcost=problem.getCostOfActions(path[childstate[0]])+heuristic(childstate[0],problem)
                    if prevcost > cost :
                        del path[childstate[0]]
                        path[childstate[0]]=p1
                        fringe.update(childstate,cost)



            """print "\n","searching"""
    if i==0 :
        print "\n","search failed"
    else :
        return path[state[0]]


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
