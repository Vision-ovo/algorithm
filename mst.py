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

        # self.array[0][3] =5
        # self.array[0][1] = 7
        # self.array[1][3] = 9
        # self.array[1][2] = 8
        # self.array[1][4] = 7
        # self.array[2][4] = 5
        # self.array[3][5] = 6
        # self.array[3][4] = 15
        # self.array[4][5] = 8
        # self.array[4][6] = 9
        # self.array[5][6] = 11

        # self.array[3][0] =5
        # self.array[1][0] = 7
        # self.array[3][1] = 9
        # self.array[2][1] = 8
        # self.array[4][1] = 7
        # self.array[4][2] = 5
        # self.array[5][3] = 6
        # self.array[4][3] = 15
        # self.array[5][4] = 8
        # self.array[6][4] = 9
        # self.array[6][5] = 11
    def creat_graph(self):
        """创建无向图图矩阵"""
        for i in range(self.edges):
            temp1 = int(input(f'请输入第{i + 1}条边的一个点:'))
            temp2 = int(input("另一个点:"))
            temp3 = int(input("长度:"))
            self.array[temp1][temp2] = temp3  #无向图
            self.array[temp2][temp1] = temp3  

        
        '''''
        self.array[0][1] = 6
        self.array[1][0] = 6
        self.array[2][0] = 1
        self.array[3][0] = 5
        self.array[4][1] = 3
        self.array[2][1] = 5
        self.array[0][2] = 1
        self.array[1][2] = 5
        self.array[3][2] = 5
        self.array[4][2] = 6
        self.array[5][2] = 4
        self.array[0][3] = 5
        self.array[2][3] = 5
        self.array[5][3] = 2
        self.array[1][4] = 3
        self.array[2][4] = 6
        self.array[5][4] = 6
        self.array[2][5] = 4
        self.array[3][5] = 2
        self.array[4][5] = 6
        '''''
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
            graph = find_path(graph,vertexs[i],list(mst_dict.values())[i])

def find_path(graph,vertex,edges):
    tmp_list = sum(graph.mst_vertex,())
    
    if vertex[0] in tmp_list and vertex[1] in tmp_list:
        for tree in graph.mst_vertex:
            if vertex[0] in tree and vertex[1] in tree:
                return graph
        temp1 = find_num(vertex[0],graph.mst_vertex)
        temp2 = find_num(vertex[1],graph.mst_vertex)
        temp3 = [graph.mst_vertex[x] for x in range(len(graph.mst_vertex)) if x != temp1 and x != temp2]
        temp3.append(sum([graph.mst_vertex[temp1],graph.mst_vertex[temp2]],()))
        graph.mst_vertex = temp3
        graph.mst_edges.append(f'V{vertex[0]} -> V{vertex[1]}:{edges}')
    elif vertex[0] in tmp_list or vertex[1] in tmp_list:
        temp1 = find_num(vertex[0],graph.mst_vertex) if vertex[0] in tmp_list else find_num(vertex[1],graph.mst_vertex)
        temp2 = [graph.mst_vertex[x] for x in range(len(graph.mst_vertex)) if x != temp1]
        temp2.append(tuple(set(sum([graph.mst_vertex[temp1],vertex],()))))
        graph.mst_vertex = temp2
        graph.mst_edges.append(f'V{vertex[0]} -> V{vertex[1]}:{edges}')
    else:
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
    