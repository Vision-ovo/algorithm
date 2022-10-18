import numpy as np
class Graph():
    def __init__(self,vertex,edges):
        self.vertex = vertex #顶点
        self.edges = edges #边
        self.array = np.full((vertex,vertex),0) #图
        self.cost = [0] * self.vertex #cost[num] 表示以num为起点到终点的最短距离
        self.paths = [[] for i in range(self.vertex)] #paths[num] 表示以num为起点到终点的最短路径
    def creat_graph(self):
        """创建图矩阵"""
        for i in range(self.edges):
            temp1 = int(input(f'请输入第{i + 1}条边的起点:'))
            temp2 = int(input("终点:"))
            temp3 = int(input("长度:"))
            self.array[temp1][temp2] = temp3
    def dynamic_programming(self):
        """动态规划算法,寻找最优路径"""
        self.paths[-1] = [self.vertex-1]
        for j in range(self.vertex-2,-1,-1): #逆序
            d = [] #用来存储长度
            process = [] #用来存储点
            for i in range(self.vertex):
                if self.array[j][i] != 0:
                    d.append(self.cost[i] + self.array[j][i])
                    process.append(f'{j}->{self.paths[i][0]}')
            self.cost[j] = min(d) #取最小值
            temp = [i for i in range(len(d)) if d[i] == self.cost[j]]
            for x in temp: #不同的路径却又相同的值
               self.paths[j].append(process[x])
if __name__ == '__main__':
    vertex = int(input("请输入图的顶点的个数:"))
    edges = int(input("请输入图的边的个数:"))
    dp = Graph(vertex,edges)
    dp.creat_graph()
    dp.dynamic_programming()
    print("最优路径:")
    for i in dp.paths[0]:
        print(f'{i},总长度:{dp.cost[0]}')
    
    