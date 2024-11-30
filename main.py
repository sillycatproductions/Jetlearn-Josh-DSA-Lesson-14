# class start -------------------------------------0

class Graph: #graph
    def __init__(self, V): #V is just a placeholder
        self.V = V
        self.adj = [[] for i in range(V)]

    def DFS(self, temp, v, visited): #dfs function
        visited[v] = True #if v has been visited
        temp.append(v) #add v to temporary list

        for i in self.adj[v]:
            if visited[i] == False: #if i hasn't been visited
                temp = self.DFS(temp, i, visited) #recall dfs function into temporary list
        return temp #recall temporary list
    
    def createEdge(self, v, w): #create a  node connection with 2 nodes
        self.adj[v].append(w) #2 nodes
        self.adj[w].append(v) #2 nodes

    def count(self): #counting how many connections are in temporary list
        visited = [] #empty visited
        cc = [] #empty count
        for i in range(self.V): #for every node
            visited.append(False) #don't add anything to visited

        for v in range(self.V): #for every node in the list
            if visited[v] == False: #if the visited has no nodes
                temp = [] #empty temporary list
                cc.append(self.DFS(temp, v, visited)) #add count
        return cc #return count

# class end ---------------------------------------0

# object ---------------------0

a = Graph(100001) #placeholder graph

a.createEdge(1, 0) #creating edge
a.createEdge(2, 3) #line 39
a.createEdge(3, 4) #line 39
a.createEdge(2, 5) #line 39
a.createEdge(5, 7) #line 39
a.createEdge(10, 100000) #line 39
a.createEdge(10, 673) #line 39
a.createEdge(175, 673) #line 39

cc = a.count() #cc = count
print('Connected Nodes: ') #print output
print(cc) #print output

