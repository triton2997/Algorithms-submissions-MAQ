import random
import numpy as np

def count_min_cut(V):
    min_cut = np.Infinity
    for key in V.keys():
        if len(V[key]) < min_cut:
            min_cut = len(V[key])

    return min_cut

def delete_self_loops(V, E):
    for key in V.keys():
        new_list = [node for node in V[key] if node != key]
        V[key] = new_list
    
    for (i,j) in E:
        if i == j:
            E.remove((i,j))
    
    return V, E

def contract_edge(V, E, index):
    u = E[index][0]
    v = E[index][1]
    new_list = [u if x == v else x for x in V[u]]
    V[u] = new_list
    for node in V[v]:
        V[u].append(node)
    for key in V.keys():
        if key == u:
            continue
        else:
            V[key] = [u if x == v else x for x in V[key]]
    new_E = []
    for (i,j) in E:
        if i == v:
            if u != j:
                changed_edge = (u,j)
                new_E.append(changed_edge)
        elif j == v:
            if u != i:
                changed_edge = (i,u)
                new_E.append(changed_edge)
        else:
            new_E.append( (i,j) )
    E = new_E
    V.pop(v)
    V, E = delete_self_loops(V,E)
    
    return V, E
    

def  randomized_min_cut(V, E):
    global min_cut
    while(len(V) > 2):
        V, E = contract_edge(V, E, random.randint(0,len(E)-1))
    cut = count_min_cut(V)
    if cut < min_cut:
        min_cut = cut

min_cut = np.Infinity
NO_OF_ITERATIONS = 50
with open('kargerMinCut.txt') as f:
    file_data = f.readlines()

for i in range(NO_OF_ITERATIONS):
    V_original = {}
    E_original = []

    for data_line in file_data:
        line = [int(x) for x in data_line.strip().split('\t')]
        u = line[0]
        V_original[u] = []
        for v in range(1,len(line)):
            V_original[u].append(line[v])
            E_original.append((u,line[v]))
    print('Iteration {}'.format(i+1))
    randomized_min_cut(V_original, E_original)
    print('Cut found: {}\n'.format(min_cut))

print('Min cut is {}'.format(min_cut))
