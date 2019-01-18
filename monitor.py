"""
日本某网站算法题 A级难度
测试结果：7/10通过，3个没通过原因尚且不明。

问题描述：
在一个h*w的网格（美术馆模型）中放置m个摄像头，n幅作品
首行输入h w m n
对于每一个摄像头，输入该摄像头的位置坐标x，y（网格左下角为原点），摄像头正对角度t（以x轴正方向为起点），摄像头广角d，和可监视半径r
对于每一个作品，输入作品坐标x1，y1
判断每一个作品是否至少在一个摄像头的监控范围内，并输出yes或no

"""


from math import sqrt, radians, asin, pi

conditions=input()
con_list = conditions.split(' ')
h = int(con_list[0])
w = int(con_list[1])
m = int(con_list[2])
n = int(con_list[3])

mon_dict = dict()
for i in range(m):
    mon = input().split(' ')
    x = int(mon[0])
    y = int(mon[1])
    t = int(mon[2])
    d = int(mon[3])
    r = float(mon[4])
    mon_dict[i]=dict()
    mon_dict[i]['x']=x
    mon_dict[i]['y']=y
    mon_dict[i]['t']=t
    mon_dict[i]['d']=d
    mon_dict[i]['r']=r

pic_dict = dict()
for j in range(n):
    coor = input().split(' ')
    x1 = int(coor[0])
    y1 = int(coor[1])
    pic_dict[j]=dict()
    pic_dict[j]['x1'] = x1
    pic_dict[j]['y1'] = y1

result_dict=dict()
for j in range(n):
    #对于每一个作品
    for i in range(m):
        #对于每一个摄像头
        #计算作品到摄像头距离
        dx = pic_dict[j]['x1'] - mon_dict[i]['x']
        dy = pic_dict[j]['y1'] - mon_dict[i]['y']
        dis = sqrt(dx**2 + dy**2)
        if dis == 0:
            result_dict[j]='yes'#特殊情况讨论
        
        if dis > mon_dict[i]['r']:
            #判断条件1是否满足（在监视距离内）
            con1 = False
        else:
            con1 = True
        #求摄像头角度范围（单位：弧度）
        low = mon_dict[i]['t'] - mon_dict[i]['d']/2
        up = mon_dict[i]['t'] + mon_dict[i]['d']/2
        rlow = radians(low)
        rup =radians(up)
        #求作品以摄像头为圆心，x轴正方形为起点的角度（单位：弧度）
        if dis != 0:
            target = asin(abs(dy)/dis)
        else:
            target = 0
            
        if dx < 0 and dy > 0:
            target = pi - target
        elif dx < 0 and dy < 0:
            target = pi + target
        elif dx > 0 and dy < 0:
            target = pi*2 - target
        elif dx == 0 and dy >= 0:
            target = pi/2
        elif dx == 0 and dy <= 0: 
            target = 1.5*pi
        elif dx >= 0 and dy == 0: 
            target = 0
        elif dx <= 0 and dy == 0: 
            target = pi
        #判断条件2是否满足（在监视角度内）
        if target >= rlow and target <= rup:
            con2 = True
        else:
            con2 = False
        
        if con1 and con2:
            result_dict[j]='yes'

result = ['no']*n
for num in result_dict:
    result[num] = 'yes'

for thing in result:
    print(thing)
