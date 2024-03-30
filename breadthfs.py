from pyamaze import maze,agent
def BFS(m):
    start=(m.rows,m.cols)
    frontier=[start]
    explored=[start]
    bSearch=[start]
    fwdPath=[] # fwdPath a list that contains the forward path from the start point to the end point
    parents = {start: None} # parents tuple contains each point with its parent (gives the ability to apply backtracking using the parent of the current node)
    while len(frontier)>0:
        currCell=frontier.pop(0)
        if currCell==(1,1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bSearch.append(childCell)
                parents[childCell] = currCell

    # backtracking from the goal to the starting point
    current = (1, 1)
    while current is not None:
        fwdPath.append(current)
        current = parents[current]
    # fwdPath starts from end point (goal) and ends with the start point (m.rows, m.cols) which is the defined starting point as shown above in line 3
    # so we have to reverse it to have the right path direction to be followed by the agent b in line 50
    fwdPath.reverse()

    # returning bSearsh and fwdPath
    return (bSearch, fwdPath)

if __name__=='__main__':
    m=maze(15,15)
    m.CreateMaze(loopPercent=10, theme="light")
    # bsSearch => BFS(m)[0] , fwdPath => BFS(m)[1]
    bSearch, fwdPath=BFS(m)
    print(bSearch)
    a=agent(m,shape="square",footprints=True,filled=True)
    b=agent(m,shape="square",footprints=True,filled=False)

    m.tracePath({a:bSearch} , delay=50, kill=True)
    m.tracePath({b:fwdPath} , delay=50)
    
    m.run()