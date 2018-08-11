# wireless-sensor-network-by-JAVA
无线传感网络程序集
---
java + python + matlib 实现  
  
## 实验一: 
### 无线传感网络连通性测试：
```
  （1）在不同节点数目n情况下，用Matlab拟合出连通率与通信半径的关系曲线。  
  （2）在不同通信半径R情况下，用Matlab拟合出连通率与节点数量n的关系曲线。 
```
#### 实验过程
```
（1）在不同节点数目下，判断连通率与通信半径的关系：
a.	在一个边长为1的正方形区域，随机撒N个节点，即通过rand函数随机生成节点X、Y轴坐标从而生成随机节点
b.	改变通信半径R，从0.01每次递增0.01直到达到1
c.	遍历生成的随机节点，根据sqrt函数求得两点间的距离r，判断r与R的大小关系；若r<R,则点联通；若r>R，则点不连通；
d.	根据随机节点的连通性判断来创建邻接矩阵p
e.	通过快速wars hell算法判断图连通性，求p,p^2,....直到p的n-1阶矩阵，将所有矩阵相加；若矩阵中存在0元素，则判断图不连通；反之，则判断图连通
f.	重复上述实验1000次，将图连通的次数与实验次数1000次相处，即得到了连通率
（2）在不同通信半径下，判断连通率与节点数目的关系：
a.在边长为1的正方形区域内，给定通信半径R;
b,改变节点数目N，从1每次递增1直到达到100;
c.根据节点数目N，通过rand(n,2,1)创建随机节点，矩阵第一列为节点X轴坐标，矩阵第二列为节点Y轴坐标;
d.遍历生成的随机节点，根据sqrt函数求得两点间的距离r，判断r与给定R的大小关系；若r<R,则点联通；若r>R，则点不连通；
e.根据随机节点的连通性判断来创建邻接矩阵p
f.通过快速wars hell算法判断图连通性，求p,p^2,....直到p的n-1阶矩阵，将所有矩阵相加；若矩阵中存在0元素，则判断图不连通；反之，则判断图连通
g.重复上述实验1000次，将图连通的次数与实验次数1000次相处，即得到了连通率
```

![1-1](../Python-lifecat/wireless_network/wsn_java/WSNimage/1-1.png)

![1-2](../Python-lifecat/wireless_network/wsn_java/WSNimage/1-2.png)

## 实验二:  
### 无线传感网络覆盖率测试:
```
  （1）给定传感器网络规模（即节点数目n）和能级，用matlab绘出网络的覆盖图；
  （2）给定传感器网络规模（即节点数目n），用matlab拟合出网络覆盖率与能级之间的关系折线图。
```
#### 实验过程
```
（1）步骤描述
A. 给定节点数目n = 100，通信半径R=0.1~0.3（R基于实验一的结果，100个随机节点，通信半径在0.1~0.3之间可实现连通）
B. 在一个边长为1的正方形区域，随机撒100个节点，即通过rand函数随机生成节点X、Y轴坐标从而生成随机节点；
C.判断随机网络是否连通，如连通执行下步，否则返回A
D. 将边长为1的正方形区域，划分成100*100网格，将网格的交点作为实验对象点；
E. 在网格中，从上到下，从左到右遍历各交点，，根据sqrt函数求得每一个交点到100个随机节点的距离r,判断r与R的大小关系；若r<R,则此交点被覆盖；若r>R，则交点不被覆盖；
F. 将被覆盖的交点个数N / 总交点数100*100，即为所要求得传感器网络的覆盖率；
G. 多次改变所给定的通信半径R的值，求得其覆盖率；
```

![2-1](../Python-lifecat/wireless_network/wsn_java/WSNimage/2-1.png)

![2-2](../Python-lifecat/wireless_network/wsn_java/WSNimage/2-2.png)

![2-3](../Python-lifecat/wireless_network/wsn_java/WSNimage/2-3.png)

## 实验三:  
实现语言：python
使用库：numpy  matplotlib

### 实验要求描述：
#### 1、给定场景，给定WSN的节点数目，节点随机分布，能按照LEACH的介绍，实现（每一轮）对WSN的分簇。请记录前k轮（eg.k=10）/ 绘制第k轮时，网络的分簇情况，即每个节点的角色（簇头or簇成员）及其关系，如是簇成员，标记其所属的簇头
Note要求：
    节点数目不宜过小；每轮只完成分簇，不考虑通信过程；每轮可以以定时器确定，也可以以完成当轮分簇为准；簇成员在寻找簇头时，以距离作为接收信号强弱的判断依据；当选为簇头的节点将，以后几轮的分簇中将，不再成为簇头，这个约束条件，在仿真中应能体现。  

#### 2、根据个人情况完成进阶实验：基于前面的实验过程，增加能量有效性的控制。
  情况1：给定所有节点具有相同的能量，考查第一个节点能量耗尽出现在第几轮。
  情况2：节点具有不同的能量，考查第一个节点能量耗尽出现在第几轮。  
  
  Note：可参考如下设计，可以不局限于如下设计。  
  
  对于节点的能量和能量消耗可以简化处理：节点初始能量为整数（eg.5000mJ）,节点的能量消耗仅考虑关键的几次通信过程，其他能量消耗不计。
  几次通信过程”：

  setup：簇成员：每收1个候选簇头信息，则能量-1，每个候选簇头仅被收集1次；通知簇头成为其成员，发送信息-2。
            候选簇头：被簇成员接收信息，即发送信息，则能量-2；被通知成为簇头，接收信息-1。
  Steady：每个簇成员每轮向簇头发送10次数据，每次成员能量-2，簇头能量-1。

![3-1](../Python-lifecat/wireless_network/wsn_java/WSNimage/3-1.png)

### 实验一算法描述：
#### 1、主程序
```python
def run():  
    """ 
    1、输入节点个数N 
    2、node_factory(N): 生成N个节点的列表 
    3、classify(nodes,flag,k=10): 进行k轮簇分类，flag已标记的节点不再成为簇首，返回所有簇的列表 
    4、show_plt(classes): 迭代每次聚类结果，显示连线图 
 
    :return: 
    """  
    N=100  
    # N = int(input("请输入节点个数:"))  
    # 获取初始节点列表，选择标志列表  
    nodes, flag = node_factory(N)  
    # 对节点列表进行簇分类，k为迭代轮数  
    iter_classes = claasify(nodes, flag, k=10)  
  
    for classes in iter_classes:  
        # 显示分类结果  
        show_plt(classes)  
```
#### 2、判断距离函数
```python
def dist(v_A, v_B):  
    """ 
    判断两个节点之间的一维距离 
    :param v_A: A 二维向量 
    :param v_B: B 二维向量 
    :return: 一维距离 
    """  
    return np.sqrt(np.power((v_A[0] - v_B[0]), 2) + np.power((v_A[1] - v_B[1]), 2))  
```

#### 3、生成随机节点集
```python
def node_factory(N):  
    """ 
    生成N个节点的集合 
    :param N: 节点的数目 
    :param nodes: 节点的集合 
    :param selected_flag: 标志:是否被选择为簇首-->初始化为0 
    :return: 节点集合nodes=[[x,y],[x,y]...] + 标志falg 
    """  
    nodes = []  
    selected_flag = []  
    for i in range(0, N):  
        # 在1*1矩阵生成[x,y]坐标  
        node = [np.random.random(), np.random.random()]  
        # print("生成的节点为:", node)  
        nodes.append(node)  
        # 对应的选择标志初始化为0  
        selected_flag.append(0)  
  
    # print("生成:", len(nodes), "个节点")  
    # print("初始化标志列表为", selected_flag)  
    return nodes, selected_flag  
```

#### 4、根据LEACH算法选择簇头节点
```python
def sel_heads(r, nodes, flags):  
    """ 
    根据阈值选取簇头节点 
    :param r: 轮数 
    :param nodes: 节点列表 
    :param flags: 选择标志 
    :param P: 比例因子 
    :return: 簇首列表heads,簇成员列表members 
    """  
    # 阈值函数 Tn 使用leach计算  
    P=0.05*(100/len(nodes))  
    Tn = P / (1 - P * (r%(1/P)))  
    # print("阈值为:", Tn)  
  
    # 簇首列表  
    heads = []  
    # 簇成员列表  
    members = []  
    # 本轮簇首数  
    n_head = 0  
  
    # 对每个节点生成对应的随机数  
    rands = [np.random.random() for _ in range(len(nodes))]  
    # print("随机数为:", rands)  
  
    # 遍历随机数列表，选取簇首  
    for i in range(len(nodes)):  
        # 若此节点未被选择为簇首  
        if flags[i] == 0:  
            # 随机数低于阈值-->选为簇首  
            if rands[i] <= Tn:  
                flags[i] = 1  
                heads.append(nodes[i])  
                n_head += 1  
                # print(nodes[i], "被选为第", n_head, "个簇首")  
            # 随机数高于阈值  
            else:  
                members.append(nodes[i])  
        # 若此节点已经被选择过  
        else:  
            members.append(nodes[i])  
  
    print("簇首为:", len(heads), "个")  
    print("簇成员为:", len(members), "个")  
  
    return heads, members  
```
#### 5、节点分簇算法
```python
def claasify(nodes, flag, k=1):  
    """ 
    进行簇分类 
    :param nodes: 节点列表 
    :param flag: 节点标记 
    :param k: 轮数 
    :return: 簇分类结果列表 classes[[类1..],[类2...],......]  [类1...簇首...簇成员] 
    """  
    # k轮的集合  
    iter_classes = []  
    # 迭代r轮  
    for r in range(k):  
        # 获取簇首列表，簇成员列表  
        heads, members = sel_heads(r, nodes, flag)  
  
        # 建立簇类的列表  
        classes = [[] for _ in range(len(heads))]  
  
        # 将簇首作为首节点添加到聚类列表中  
        for i in range(len(heads)):  
            # print("第", i + 1, "个簇首为", heads[i])  
            classes[i].append(heads[i])  
  
        # print("簇首集合:", classes)  
  
        # 簇分类:遍历节点node  
        for n in range(len(members)):  
  
            # 选取距离最小的节点  
            dist_min = 1  
  
            for i in range(len(heads)):  
                dist_heads = dist(members[n], heads[i])  
  
                # 找到距离最小的簇头对应的heads下标i  
                if dist_heads < dist_min:  
                    dist_min = dist_heads  
                    head_cla = i  
            # 0个簇首的情况  
            if dist_min==1:  
                print("本轮没有簇首!")  
                break  
  
            # 添加到距离最小的簇首对应的聚类列表中  
            classes[head_cla].append(members[n])  
  
        # 将簇首作为首节点添加到聚类列表中  
        # for i in range(len(classes)):  
            # print("第", i + 1, "类包含:", classes[i])  
  
        iter_classes.append(classes)  
  
    return iter_classes  
```

#### 6、绘制分类图
```python
def show_plt(classes):  
    """ 
    显示分类图 
    :param classes: [[类1...],[类2...]....]-->[簇首,成员,成员...] 
    :return: 
    """  
    fig = plt.figure()  
    ax1 = plt.gca()  
  
    # 设置标题  
    ax1.set_title('WSN1')  
    # 设置X轴标签  
    plt.xlabel('X')  
    # 设置Y轴标签  
    plt.ylabel('Y')  
  
    icon = ['o', '*', '.', 'x', '+', 's']  
    color = ['r', 'b', 'g', 'c', 'y', 'm']  
  
    # 对每个簇分类列表进行show  
    for i in range(len(classes)):  
        centor = classes[i][0]  
        # print("第", i + 1, "类聚类中心为:", centor)  
        for point in classes[i]:  
            ax1.plot([centor[0], point[0]], [centor[1], point[1]], c=color[i % 6], marker=icon[i % 5], alpha=0.4)  
  
    # 显示所画的图  
    plt.show()  
```
