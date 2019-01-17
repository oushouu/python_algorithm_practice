"""
来源：某日本编程网站（不让公开原题） 难度：A级
代码运行结果：我写的以下代码并没有通过全部的测试案例，但我始终没有发现问题在哪，因为我觉得这个算法的逻辑是很严谨的。

问题描述：
给一个h（高）*m（宽）个数小正方形组成的矩形网格，每一个小正方形区域中可摆放两种方向的镜子‘/’和‘\’，或者也可以不摆镜子。
现在要让一道射线从左上角的正方形的左边射入（射线初始方向为右），当射线遇到镜子会发生折射，如向右发射的射线遇到‘/’镜子会向上折射，以此类推。
通过输入h，m来确定网格大小，然后根据网格行数输入每行的镜子布局：
1.‘/’
2.‘\’
3.‘_’（表示没有镜子）

如：
3 5
__\_/
___/_
\/\_/

要输出的是射线从进入网格到出去一共经过几次小正方形。

上述例子的结果是9次（可以执笔画图便于理解）
"""




# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
def move(now, way):
#定义一个让射线在网格中移动到下一个坐标的函数
    if way == 'right':
        now[1] += 1
    elif way == 'left':
        now[1] -= 1
    elif way == 'down':
        now[0] += 1
    elif way == 'up':
        now[0] -= 1
    return now
    
def turn(matrix, now, way):
#定义一个判断射线在当前小正方形中该往什么方向折射的函数
    if matrix[now[0]][now[1]] == '/':
        if way == 'right':
            way = 'up'
        elif way == 'left':
            way = 'down'
        elif way == 'down':
            way = 'left'
        elif way == 'up':
            way = 'right'
    elif matrix[now[0]][now[1]] == '\\':
        if way == 'right':
            way = 'down'
        elif way == 'left':
            way = 'up'
        elif way == 'down':
            way = 'right'
        elif way == 'up':
            way = 'left'
    return way
    
def if_inner(h,w,now):
#定义一个判断当前位置是否在网格内的函数
    if now[0] < 0 or now[0] > h-1 or now[1] < 0 or now[1] > w - 1:
        flag = False
    else:
        flag = True
    return flag
        
conditions = input()
con_list = list(conditions)
h = int(con_list[0])
w = int(con_list[2])
matrix = []
for row in range(h):
将网格以一个二维列表的形式保存
    mirror = input()
    mirror_list = list(mirror)
    matrix.append(mirror_list)
#初始起点条件    
now = [0, 0]# [h,m]
way = 'right'
flag = if_inner(h,w,now)
count = 0
#开始循环
while flag:
    #先判断要不要变向
    way = turn(matrix, now, way)
    #根据变向结果移动坐标
    now = move(now, way)
    #判断是否界内
    flag = if_inner(h,w,now)
    count += 1
print(count)
    


        
    
