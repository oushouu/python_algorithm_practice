"""
P站S级题目（偏简单，应该归为A级）
代码测试结果：全部通过
题目省略，草稿一并上传

输入例：
1 6 2 5 4 3 #输入色子的六个面
4 #输入格子数n
1 #从左到右依次输入n次格子的数字
5
3
4

输出例：
4 #输出色子旋转的次数
"""

touzi = input().split(' ')
t = int(touzi[0])
b = int(touzi[1])
u = int(touzi[2])
d = int(touzi[3])
l = int(touzi[4])
r = int(touzi[5])
dice = list(map(int, touzi))

def left(dice):
    t = dice[0]
    b = dice[1]
    u = dice[2]
    d = dice[3]
    l = dice[4]
    r = dice[5]
    dice[0] = u #t = u
    dice[1] = d #b = d
    dice[2] = b #u = b
    dice[3] = t #d = t


def right(dice):
    t = dice[0]
    b = dice[1]
    u = dice[2]
    d = dice[3]
    l = dice[4]
    r = dice[5]
    dice[0] = d #t = d
    dice[1] = u #b = u
    dice[2] = t #u = t
    dice[3] = b #d = b

    
def back(dice):
    t = dice[0]
    b = dice[1]
    u = dice[2]
    d = dice[3]
    l = dice[4]
    r = dice[5]
    dice[0] = l #t = l
    dice[1] = r #b = r
    dice[4] = b #l = b
    dice[5] = t #r = t

    
def front(dice):
    t = dice[0]
    b = dice[1]
    u = dice[2]
    d = dice[3]
    l = dice[4]
    r = dice[5]
    dice[0] = r #t = r
    dice[1] = l #b = l
    dice[4] = t #l = t
    dice[5] = b #r = b


n = int(input())

board = []
for i in range(n):
    mass = int(input())
    board.append(mass)

change = 0
for i in range(n):
    if board[i] == dice[0]:
        change += 0
    elif board[i] == dice[1]:
        front(dice)
        front(dice)
        change +=2
    elif board[i] == dice[2]:
        left(dice)
        change += 1
    elif board[i] == dice[3]:
        right(dice)
        change += 1
    elif board[i] == dice[4]:
        back(dice)
        change += 1
    elif board[i] ==dice[5]:
        front(dice)
        change += 1

print(change)
