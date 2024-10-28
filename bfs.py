from collections import defaultdict, deque

def bfs(tree, start, search):
    visited = set()
    queue = deque([start])
   
    path = []
    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        path.append(node)
        if node == search:
            return path
        for n in tree[node]:
            if n not in visited:
                queue.append(n)
    return path
def opath(tree,start,search):
    visited = set()
    queue = deque([(start, [start])])  

    while queue:
        node, path = queue.popleft()
       
        if node == search:
            return path  
       
        visited.add(node)
       
        for neighbor in tree[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))  
    return None  
def print_pyramid(tree, start):
    def get_level(node, level=0, levels=None):
        if levels is None:
            levels = defaultdict(list)
        levels[level].append(node)
        for child in sorted(tree[node]):
            get_level(child, level + 1, levels)
        return levels
   
    levels = get_level(start)
    max_width = len(levels[max(levels)]) * 4
   
    for level in sorted(levels):
        level_nodes = levels[level]
        spacing = max_width // (2 ** (level + 1))
        line = (" " * spacing).join(f"{node:4}" for node in level_nodes)
        print(" " * (max_width // 2 - len(line) // 2) + line)

def main():
    while True:
        try:
            n = int(input("Enter the number of nodes: "))
            if n <= 0:
                raise ValueError("Invalid input.Please enter a valid positive integer.")
            tree = defaultdict(list)
            nodes = set()
            break
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")
    print("Enter each node and its adjacent nodes (space-separated) in each line:")
    for _ in range(n):
        while True:
            line = input().strip()
            if not line:
                print("Please enter the node and its adjacent nodes.")
                continue
           
            parts = line.split()
            if len(parts) < 1:
                print("Invalid input. A node must be specified.")
                continue

            node = parts[0]
            children = parts[1:]
            tree[node].extend(children)
            nodes.add(node)
            nodes.update(children)
            break

    if not nodes:
        print("No nodes were entered.")   
    l = list(tree.keys())
    print("Available nodes:")
    print(l)
    start_node = l[0]
    print("\nTree Structure:")
    print_pyramid(tree, start_node)
    while True:
        try:
            search_node = input("\nEnter the search node: ")
            if not search_node:
                print("Invalid input. Please enter a valid node")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid node.")
    if search_node in l:
        bfs_result = bfs(tree, start_node, search_node)
        optimal=opath(tree,start_node,search_node)
        if bfs_result:
            print("Traversal: ", ' -> '.join(bfs_result))
        else:
            print("Node {search_node} not found")
    else:
        print("Node not Found")    
   
    

if __name__ == "__main__":
    main()
