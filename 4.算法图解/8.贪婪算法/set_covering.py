# 广播台覆盖州范围问题

# 目标覆盖的州名称
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

# 不同广播台覆盖范围
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

# 最终选择的广播台
final_stations = set()

# 当还有未覆盖的目标州就继续选择
while states_needed:
    # 选择覆盖最广的电台
    best_station = None
    # 包含该广播台覆盖的所有未覆盖的州
    states_covered = set()
    # 遍历所有广播台和对应的覆盖州
    for station, states in stations.items():
        # 需要覆盖的州和当前电台可覆盖的州取交集
        covered = states_needed & states
        # 如果交集面积大于最小覆盖标记
        if len(covered) > len(states_covered):
            # 记录当前电台为最优选择
            best_station = station
            # 记录当前最优电台所能覆盖的最大有效面积
            states_covered = covered
    # 需求覆盖面积删除当前最优电台覆盖面积
    states_needed -= states_covered
    # 将当前最优电台放入选择集合
    final_stations.add(best_station)

print(final_stations)  # {'kfive', 'kthree', 'kone', 'ktwo'}
