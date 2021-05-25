class Solution:
    def bfs(self, initialState, deadend, target):
        visited = set(initialState)
        queue = deque()
        queue.append((initialState, 0))
        while queue:
            curState, move = queue.popleft()
            if curState == target:
                return move
            for i in range(4):
                for turn in [1, -1]:
                    nextState = curState[:i] + str((int(curState[i]) + turn) % 10) + curState[i+1:]
                    if nextState not in visited and nextState not in deadend:
                        visited.add(nextState)
                        queue.append((nextState, move+1))
        return -1
        
    def openLock(self, deadends: List[str], target: str) -> int:
        deadend = set(deadends)
        if '0000' in deadend:
            return -1
        return self.bfs('0000', deadend, target)

# Slower
class Solution:
    def makeDeadendSet(self, deadends):
        deadend = set()
        for i in range(len(deadends)):
            deadend.add(tuple(list(deadends[i])))
        return deadend
    
    def findNext(self, state, i):
        newStateAdd = list(state).copy()
        newStateMinus = list(state).copy()
        if state[i] == '0':
            newStateAdd[i] = str('1')
            newStateMinus[i] = str('9')
        elif state[i] == '9':
            newStateAdd[i] = str('0')
            newStateMinus[i] = str('8')
        else:
            newStateAdd[i] = str(int(state[i])+1)
            newStateMinus[i] = str(int(state[i])-1)
        return tuple(newStateAdd), tuple(newStateMinus)
    
    def bfs(self, initialState, deadend, target):
        target = tuple(list(target))
        visited = set()
        queue = deque()
        queue.append([tuple(list(initialState))])
        move = 0
        while queue:
            curMove = queue.popleft()
            nextMove = []
            for curState in curMove:
                if curState == target:
                    return move
                if not (curState in deadend or curState in visited):
                    visited.add(curState)
                    for i in range(4):
                        newStateAdd, newStateMinus = self.findNext(curState, i)
                        nextMove.append(newStateAdd)
                        nextMove.append(newStateMinus)
            if not nextMove:
                return -1
            queue.append(nextMove)
            move += 1
        
    def openLock(self, deadends: List[str], target: str) -> int:
        deadend = self.makeDeadendSet(deadends)
        return self.bfs('0000', deadend, target)