graph={
    'A':[('B',6),('F',3)],
    'B':[('C',3),('D',2)],
    'C':[('E',5),('D',1)],
    'D':[('C',1),('E',8)],
    'E':[('J',5),('I',5)],
    'F':[('G',1),('H',7)],
    'G':[('I',3)],
    'H':[('I',2)],
    'I':[('J',3),('E',5)],
}
H_table={
    'A':10,
    'B':8,
    'C':5,
    'D':7,
    'E':3,
    'F':6,
    'G':5,
    'H':3,
    'I':1,
    'J':0
}
def path_f_cost(path):
    g_cost=0
    #loop to find g_cost
    for node in path:
        g_cost+=node[1]
    #the last node in the path
    last_node=path[-1][0]
    #last node cost
    h_cost=H_table[last_node]
    #total cost
    f_cost =g_cost+h_cost
    return f_cost,last_node
def A_star(graph,str,goal):
    #the visited list
    visited=[]
    #the queue list
    queue=[[(str,0)]]
    while queue:
        #sort the queue by the path cost
        queue.sort(key=path_f_cost)
        path=queue.pop(0)
        node=path[-1][0]
        #if the node in visited continue the loop
        #else append it to the visited list
        if node in visited:
            continue
        visited.append(node)
        #check if the node is the goal return the path
        #else add the adjecent of the node to the queue
        if node==goal:
            return path
        else:
            adj_nodes=graph[node]
            for (node2,cost) in adj_nodes:
                new_path=path.copy()
                new_path.append((node2,cost))
                queue.append(new_path)
solution=A_star(graph,'A','J')
print("the path is",end=" ")
for i in solution:
    print(i[0],end=" ")
print()
print("the cost ",path_f_cost(solution)[0])

