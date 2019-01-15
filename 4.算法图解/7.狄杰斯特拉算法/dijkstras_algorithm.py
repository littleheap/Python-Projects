# 图网络散列表
graph = {}  # 初始化图散列表
graph["start"] = {}  # 初始化起始节点散列表
graph["start"]["a"] = 6  # 起始节点到a节点权重为6
graph["start"]["b"] = 2  # 起始节点到a节点权重为2

graph["a"] = {}  # 初始化a节点散列表
graph["a"]["fin"] = 1  # a节点到终点权重为1

graph["b"] = {}  # 初始化b节点散列表
graph["b"]["a"] = 3  # b节点到a节点权重为3
graph["b"]["fin"] = 5  # b节点到终点权重为5

graph["fin"] = {}  # 初始化终点散列表

# 各节点开销散列表
infinity = float("inf")
costs = {}  # 初始化开销散列表
costs["a"] = 6  # 更新a节点开销为6
costs["b"] = 2  # 更新b节点开销为2
costs["fin"] = infinity  # 更新终点开销为无穷

# 父节点记录散列表
parents = {}  # 初始化父节点记录散列表
parents["a"] = "start"  # 记录a节点的父节点为起始节点
parents["b"] = "start"  # 记录b节点的父节点为起始节点
parents["fin"] = None  # 记录终点的父节点为未知

# 已处理节点记录列表
processed = []


# 寻找未处理节点中最小开销节点的函数
def find_lowest_cost_node(costs):
    # 初始化最低开销节点为正无穷
    lowest_cost = float("inf")
    # 初始化最低开销节点为未知
    lowest_cost_node = None
    # 遍历所有节点
    for node in costs:
        # 获取当前节点开销
        cost = costs[node]
        # 如果当前节点小于最低开销并且未被处理
        if cost < lowest_cost and node not in processed:
            # 记录当前得到的最低开销
            lowest_cost = cost
            # 记录当前得到的最低开销节点
            lowest_cost_node = node
    # 返回找到的未被处理的最低开销节点
    return lowest_cost_node


# 在未处理的节点中找出最小开销的节点
node = find_lowest_cost_node(costs)
# 当所有节点都被处理后结束算法
while node is not None:
    # 获取当前节点开销
    cost = costs[node]
    # 遍历当前节点所有邻居节点
    neighbors = graph[node]
    for n in neighbors.keys():
        # 计算邻居节点新开销
        new_cost = cost + neighbors[n]
        # 比较原始开销和新开销大小
        if costs[n] > new_cost:
            # 如果原始开销大于新开销则更新该节点开销
            costs[n] = new_cost
            # 当前节点变为邻居节点的父节点
            parents[n] = node
    # 标记当前节点为已处理
    processed.append(node)
    # 找到下一个要处理的节点
    node = find_lowest_cost_node(costs)

print("Cost from the start to each node:")
print(costs)  # {'a': 5, 'b': 2, 'fin': 6}
