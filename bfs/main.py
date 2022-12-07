import ast
with open("bfs") as bfs:
    graph=ast.literal_eval(bfs.read())
visited = [] # List for visited nodes.
queue = [] # Initialize a queue
def bfs( graph, node): # function for BFS
   visited.append(node)
   queue.append(node)
   while queue: # Creating loop to visit each node
       node = queue.pop(0)
       print(node, end=" ")
       for neighbour in graph[node]:
          if neighbour not in visited:
               visited.append(neighbour)
               queue.append(neighbour)
print("Following is the Breadth-First Search")
bfs( graph, '5') 