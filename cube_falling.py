"""
来源：日本某编程网站，不让公开原题信息，难度B级（实际可以算A级了）
代码测试结果：全部通过

题目大意：
在一个h*w（纵向*横向）个正方形组成的矩形网格中，不断有底面和正方形大小相同的正方体落下，落点必须是完全落入某一个正方形中，落点坐标可以自由选择。
两次相同落点上的正方体可以叠加，只不过当该位置四周有水平面更低的正方形各自存在时，该正方体必须向更低的格子里移动，
当相邻的东南西北四个方向的正方形区域中的多个都满足此条件时，优先移动顺序为北，东，南，西。
若移动后发现四周仍有更低位置的正方形区域，这继续按照上述柜子移动

输入网格大小信息以及落下正方体个数
输出最终网格布局（每个位置上叠加的正方体个数）

"""

# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

def create_direct(x,y,matrix):
    direct = []
    current_high = matrix[y-1][x-1]
    direct.append(current_high)
    if y-2 >= 0:
        north = matrix[y-2][x-1]
    else: 
        north = None
    direct.append(north)
    if x <= w-1:
        east = matrix[y-1][x]
    else: 
        east = None
    direct.append(east)
    if y <= h-1:
        south = matrix[y][x-1]
    else: 
        south = None
    direct.append(south)
    if x-2 >= 0:
        west = matrix[y-1][x-2]
    else:
        west = None
    direct.append(west)
    return direct

def choose_way(direct):    
    i = 1
    cur = direct[0]
    move_direct = 0
    while i < len(direct):
        if direct[i] != None:
            if cur - direct[i] > 0:
                move_direct = i
                break
            else:
                i += 1
        else:
            i += 1
    return move_direct


conditions = input()
con_list = conditions.split(' ')
h = int(con_list[0])
w = int(con_list[1])
n = int(con_list[2])
row = [0] * w
matrix = []
for r in range(h):
    matrix.append(row[:])
for t in range(n):
    location = input()
    coor = location.split(' ')
    x = int(coor[0])
    y = int(coor[1])
    
    while True:
        direct = create_direct(x,y,matrix)
    
        move_direct = choose_way(direct)
        
        if move_direct == 0:
            matrix[y-1][x-1] += 1
            break
        elif move_direct == 1:
            #matrix[y-2][x-1] += 1
            y = y - 1
        elif move_direct == 2:
            #matrix[y-1][x] += 1
            x = x + 1
        elif move_direct == 3:
            #matrix[y][x-1] += 1
            y = y + 1
        elif move_direct == 4:
            #matrix[y-1][x-2] += 1
            x = x - 1
        


for r in matrix:
    line = ' '.join(str(e) for e in r)
    print(line)
        

    
    
    
