from collections import deque


# 检测是否为目标对象
def person_is_seller(name):
    return name[-1] == 'm'


# 创建图信息的节点散列表
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


# 广度优先搜索函数
def search(name):
    # 初始化队列
    search_queue = deque()
    # 将当前对象的邻居放入队列
    search_queue += graph[name]
    # 记录已搜寻的路径信息列表
    searched = []
    while search_queue:
        # 头对象出队
        person = search_queue.popleft()
        # 确认当前出队对象未被检索
        if person not in searched:
            # 检测是否为目标搜寻对象
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                # 如果不是，将当前对象的邻居放入搜寻队列
                search_queue += graph[person]
                # 标记当前对象为已搜寻
                searched.append(person)
    return False


search("you")  # thom is a mango seller!
