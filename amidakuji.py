"""
日本某网站A级算法题：题目不能透露，只能把草稿一并上传，不然我怕忘记题目是什么
代码测试结果：全部通过
输入例：
7 4 5   # l,n,m
1 3 1   #第二行开始是a,b,c  （起始纵线，横线左端顶部距离，横线右端到顶部距离）
3 2 2
2 3 5
3 4 4
1 6 6

输出例：
3  #表示从第三根纵线落下的求最终会通过最左边的那跟纵线（落下规则：垂直下落，遇到横线则移动到横线另一端）
"""

conditions = input()
con_list = conditions.split(' ') #输入纵线长度l，纵线条数n，横线条数m
l = int(con_list[0])
n = int(con_list[1])
m = int(con_list[2])

pair = dict()  #创建空字典pair用于存放横线两端对应坐标
for i in range(m):
    line = input().split(' ')
    a = int(line[0])
    b = int(line[1])
    c = int(line[2])
    pair[(a-1, b)] = (a, c)
    pair[(a, c)] = (a-1, b)
    

now = (0, l) #当前坐标（左上角为原点），起点为左下角（题目所说的终点，注意纵坐标是L不是1）
while now[1] != 0:  当当前坐标的纵坐标不小于零
    if now not in pair:  #若当前坐标上没有横线，则坐标上移一格
        now = list(now)
        now[1] = now[1] - 1
        now = tuple(now)
    else: #若当前坐标处于横线的一端，则移动到横线另一端并上移一格
        now = pair[now]
        now = list(now)
        now[1] = now[1] - 1
        now = tuple(now)
print(now[0] + 1)
