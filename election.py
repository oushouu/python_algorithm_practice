"""
这是一道paiza上的B Rank的题，背景是一个简单的竞选演讲逻辑，由于paiza不让公开题目内容，这里只能放我自己写的代码。
不过就算没有题干，只要能完全理解代码的含义，题干也是可以推测的。

输入规则是题目给定的，如：

input：
3 3 4 
1
1
2
3
第0行输入一个字符串‘3 3 4’，分别代表参选人数，参与投票人数，与演讲次数；
第1行开始输入每次演讲人的编号，输入行数等于第0行中最后一个参数的值，即演讲次数

output：
3
最后要求返回得票最多的演讲者编号，若最高得票数相同需要返回多个候选人编号

"""


conditions = input() #输入条件
con_list = conditions.split(' ') #将条件里的三个参数信息提取并放入一个list
m = int(con_list[0]) #将list中的三个参数转为int类型，并各自带入三个变量，即表m参选人数，n参与投票人数，与k演讲次数
n = int(con_list[1])
k = int(con_list[2])
m_count = [0] * m  #创建一个元素个数等于候选人数的空list，用来表示各个候选人的得票情况，最初都是0
independent = n  #设一个independent变量用于表示还没有觉得支持哪位候选人的投票者人数，初始值是n
for i in range(k):  #在k次演讲中：
    m_id = int(input())-1  #每次要求用户输入一个参与本次演讲的候选人编号，并转化成在m_count列表中的位置
    if independent != 0:  #当中立投票者人数不为零时
        independent -= 1   #中立池人数减一
        m_count[m_id]  +=1   #演讲者得票加一
    index = 0  #设另一变量index来表示演讲者以外的其他候选人在m_count列表中的位置，初始为0
    while index < m:  #当index没有超过候选者总人数时进行迭代：
        if index != m_id and m_count[index] > 0:  #当index不是演讲者，且此时该index位置上的票数大于0时：
            m_count[index] -= 1 #该竞选者票数减一
            m_count[m_id]  +=1  #演讲者票数加一
        index += 1 #位置往后移动一位
result = max(m_count) #计算最大得票数
for j in range(m):  #若m_count中有人的得票数等于最大得票数，print该候选人的编号
    if m_count[j] == result:
        print(j+1)
