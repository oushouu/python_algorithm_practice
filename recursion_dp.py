"""
例题：
f(k) = 'ABC'  , k=1时
f(k) = 'A' + f(n-1) + 'B' + f(n-1) + 'C' , k>1时
求任意f(n)结果中第s到t个字母
"""




conditions = input()
con_list = conditions.split(' ')
k = int(con_list[0])
s = int(con_list[1])
t = int(con_list[2])
"""
#方法1：递归函数（自己套用自己），性能差，运算量大
def abc(n):
    if n ==1:
        y = 'ABC'
        return y
    elif n > 1:
        return 'A'+abc(n-1)+'B'+abc(n-1)+'C'

#方法2：备忘录算法（记录每一项结果并输出末项），比递归好一点，但也不太行
def abc(n):
    if n ==1:
        y = 'ABC'
        return y
    elif n > 1:
        #return 'A'+abc(n-1)+'B'+abc(n-1)+'C'
        a = ['ABC']
        for i in range(n-1):
            a.append('A'+a[-1]+'B'+a[-1]+'C')
        return a[-1]
"""
#方法3：动态规划（Dynamic Programing），不确定DP算法说的是不是这个意思，但是代码上看起来这是最返璞归真的
#（也是我一开始不知道递归算法前唯一会写的一种看起来最平常的算法，现在看起来反而最优了。。。）
def abc(n):
    y = 'ABC'
    if n == 1:
        return y
    else:
        index = 1
        while index < n:
            y_last = y
            y = 'A'+ y +'B'+ y +'C'
            index += 1
        return y
        
string=abc(k)
print(string[s-1:t])
