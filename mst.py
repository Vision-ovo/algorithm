#用矩阵实现了最小生成树树的Prim算法和Kruskal算法
import numpy as np
import random
class Graph():
    def __init__(self,vertex,edges):
        self.vertex = vertex #顶点
        self.edges = edges #边
        self.array = np.full((vertex,vertex),0) #图
        self.vertex_list = [x for x in range(vertex)]
        self.mst_vertex = []
        self.mst_edges = []

    def creat_graph(self):
        """创建无向图图矩阵"""
        for i in range(self.edges):
            temp1 = int(input(f'请输入第{i + 1}条边的一个点:'))
            temp2 = int(input("另一个点:"))
            temp3 = int(input("长度:"))
            self.array[temp1][temp2] = temp3  #无向图
            self.array[temp2][temp1] = temp3  

def mst_prim(graph):
    """prim最小生成树"""
    graph.mst_vertex.append(random.randint(0,graph.vertex-1))  #随机选取一个顶点
    while(len(graph.mst_vertex) != graph.vertex):
        tmp_edge = 9999
        for i in graph.mst_vertex: 
            for j in list(set(graph.vertex_list) ^ set(graph.mst_vertex)): #顶点集合与最小生成树点集合的差集
                if graph.array[i][j] == 0:
                    continue
                else:
                    if graph.array[i][j] < tmp_edge:
                        tmp_edge = graph.array[i][j]
                        tmp = (i,j)
        graph.mst_vertex.append(tmp[1])
        graph.mst_edges.append(f'V{tmp[0]} -> V{tmp[1]}:{tmp_edge}')
    
def mst_kruskal(graph):
    """kruskal最小生成树"""
    #在此算法中的mst_vertex可看成森林的集合
    mst_dict = {}
    for i in range(1,graph.vertex):
        for j in range(i):
            if graph.array[i][j] != 0:
                mst_dict[(i,j)] = graph.array[i][j]
    mst_dict = dict(sorted(mst_dict.items(), key=lambda x: x[1]))  #将边从小到大排序
    while(len(list(set(sum(graph.mst_vertex,())))) != graph.vertex):
        a = len(list(set(sum(graph.mst_vertex,()))))
        vertexs = list(mst_dict.keys())
        for i in range(len(mst_dict.values())):
            graph = find_tree(graph,vertexs[i],list(mst_dict.values())[i])

def find_tree(graph,vertex,edges): #判断图是否再在一棵树上
    tmp_list = sum(graph.mst_vertex,())
    
    if vertex[0] in tmp_list and vertex[1] in tmp_list:
        for tree in graph.mst_vertex:
            if vertex[0] in tree and vertex[1] in tree:  #两个点在同一颗树上
                return graph
        temp1 = find_num(vertex[0],graph.mst_vertex)  #两个点在不同的树上，加入并将两棵树连在一起
        temp2 = find_num(vertex[1],graph.mst_vertex)
        temp3 = [graph.mst_vertex[x] for x in range(len(graph.mst_vertex)) if x != temp1 and x != temp2]
        temp3.append(sum([graph.mst_vertex[temp1],graph.mst_vertex[temp2]],()))
        graph.mst_vertex = temp3
        graph.mst_edges.append(f'V{vertex[0]} -> V{vertex[1]}:{edges}')
    elif vertex[0] in tmp_list or vertex[1] in tmp_list:  #只有一个点在树上，将新加入的点加入这棵树
        temp1 = find_num(vertex[0],graph.mst_vertex) if vertex[0] in tmp_list else find_num(vertex[1],graph.mst_vertex)
        temp2 = [graph.mst_vertex[x] for x in range(len(graph.mst_vertex)) if x != temp1]
        temp2.append(tuple(set(sum([graph.mst_vertex[temp1],vertex],()))))
        graph.mst_vertex = temp2
        graph.mst_edges.append(f'V{vertex[0]} -> V{vertex[1]}:{edges}')
    else:  #点没在任何一颗树上
        graph.mst_vertex.append(vertex)
        graph.mst_edges.append(f'V{vertex[0]} -> V{vertex[1]}:{edges}')
    return graph

def find_num(target,arr):
    num = 0
    for i in arr:
        if target in i:
            return num
        num += 1
if __name__ == '__main__':
    vertex = int(input("请输入图的顶点的个数:"))
    edges = int(input("请输入图的边的个数:"))
    dp1 = Graph(vertex,edges)  #Prim
    dp2 = Graph(vertex,edges)  #kruskal
    dp1.creat_graph()
    dp2.array = dp1.array
    print("Prim算法:")
    mst_prim(dp1)
    print(dp1.mst_edges)
    print("Kruskal算法:")
    mst_kruskal(dp2)
    print(dp2.mst_edges)
    