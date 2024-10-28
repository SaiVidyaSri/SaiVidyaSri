from collections import deque

def valid(lm, lc, rm, rc):
    if lm >= 0 and rm >= 0 and lc >= 0 and rc >= 0:
        if (lm == 0 or lm >= lc) and (rm == 0 or rm >= rc):
            return True
    return False

def mc(m, c, b):
    start_state = (m, c, 0, 0, 1)  
    goal_state = (0, 0, m, c, 0)  
    
    queue = deque([(start_state, [])])
    visited = set([start_state])
    
    possible_moves = [(i, j) for i in range(b + 1) for j in range(b + 1) if 1 <= i + j <= b]
    
    while queue:
        (lm, lc, rm, rc, boat_pos), path = queue.popleft()

        if (lm, lc, rm, rc, boat_pos) == goal_state:
            return path + [(lm, lc, rm, rc, boat_pos)]


        for mm, cm in possible_moves:
            if boat_pos == 1:  
                new = (lm - mm, lc - cm, rm + mm, rc + cm, 0)
            else:  
                new = (lm + mm, lc + cm, rm - mm, rc - cm, 1)
            
            if valid(new[0], new[1], new[2], new[3]) and new not in visited:
                visited.add(new)
                queue.append((new, path + [(lm, lc, rm, rc, boat_pos)]))
    
    return None  

while True:
    try:
        lm = int(input("Enter number of missionaries: "))
        if lm <= 0:
            raise ValueError("Please enter a valid positive integer.")
        break
    except ValueError as e:
        print(f"Error: Please enter valid positive integer")

while True:
    try:
        lc = int(input("Enter number of cannibals: "))
        if lc <= 0:
            raise ValueError("Please enter a valid positive integer.")
        break
    except ValueError as e:
        print(f"Error: Please enter a valid positive integer.")

while True:
    try:
        b = int(input("Enter capacity of the boat: "))
        if b <= 0:
            raise ValueError("Please enter a valid positive integer.")
        break
    except ValueError as e:
        print(f"Error: Please Enter a valid positive integer.")
p = mc(lm, lc, b)
if p is not None:
    print([lm,lc,1],[0,0,0])
if p is not None:
    for i in range(1,len(p)):
        lmp, lcp, rmp, rcp, boat_pos = p[i-1]
        lmc,lcc,rmc,rcc,boat_pos=p[i]
        left_side = [str(lmc)+"M", str(lcc)+"C", boat_pos]  
        right_side = [str(rmc)+"M", str(rcc)+"C", 1 - boat_pos]
        if(boat_pos==1):
            print(f"step{i}: ",end=" ")
            print(f"From Right to left {abs(rmc-rmp)} Missionaries and {abs(lcc-lcp)} Canibels moved")
            print(f"{left_side} <- {right_side}")
        else:
            print(f"step{i}: ",end=" ")
            print(f"From left to right {abs(lmc-lmp)} Missionaries and {abs(rcc-rcp)} Canibels moved")
            print(f"{left_side} -> {right_side}")    
else:
    print("Not possible")
