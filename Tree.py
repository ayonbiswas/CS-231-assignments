#Tree.py

def adj_list(adj_mat):
    length = len(adj_mat)
    adjacency = dict()

    for i in xrange(1,length):
        ctr = 0
        for j in xrange(i):
            
            if adj_mat[i][j]==1:
                ctr +=1
                if(i in adjacency):
                    adjacency[i].append(j)
                else:
                    adjacency[i] = [j]
                if(j in adjacency):
                    adjacency[j].append(i)
                else:
                    adjacency[j] = [i]
        if ctr ==0:
            print "not tree"
            exit()

    print adjacency
    return adjacency

def dfs(v,visited, adj,parent):
    flag = 0
    
    visited[v]=True

    for x in range(len(adj[v])):
        
        if(visited[adj[v][x]]==False):
            print adj[v][x]
            dfs(adj[v][x], visited,adj,v)

        elif([adj[v][x]] != parent):
            
            flag = 1

    if flag ==1:
        return True
    else:
        return False
                
    
    


def cycle_detect(adj_mat):
    adj = dict()
    adj = adj_list(adj_mat)
    visited = []
    print adj
    for i in range(len(adj)):
        visited.append( False)
    ctr = 0
    print visited
    
    for i in xrange(len(adj)):
        if visited[adj.keys()[i]]==False:
            
            ctr+=1
            k = dfs(i,visited,adj,-1)
            
            if(k == True):
                print "not tree"
                exit()
            else:
                 print "tree"
                 exit()
             
    if(ctr >1):
        print"not tree"
    else:
        print"tree"
in_adj = input("input adjacency matrix?")
cycle_detect(in_adj)
            
