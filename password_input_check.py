"""
牛客网：
2018校招真题：密码检查


题目描述
小明同学最近开发了一个网站，在用户注册账户的时候，需要设置账户的密码，为了加强账户的安全性，小明对密码强度有一定要求：

1. 密码只能由大写字母，小写字母，数字构成；

2. 密码不能以数字开头；

3. 密码中至少出现大写字母，小写字母和数字这三种字符类型中的两种；

4. 密码长度至少为8

现在小明受到了n个密码，他想请你写程序判断这些密码中哪些是合适的，哪些是不合法的。

输入描述:
输入一个数n，接下来有n(n≤100)行，每行一个字符串，表示一个密码，输入保证字符串中只出现大写字母，小写字母和数字，字符串长度不超过100。
输出描述:
输入n行，如果密码合法，输出YES，不合法输出NO
示例1
输入
1
CdKfIfsiBgohWsydFYlMVRrGUpMALbmygeXdNpTmWkfyiZIKPtiflcgppuR
输出
YES
"""
n = int(input())
results = []
for i in range(n):
    line = input()
    line_list = list(line)
    #条件1
    for e in line_list:
        if e.isupper():
            f1 = True
        elif e.islower():
            f1 = True
        else:
            try:
                int(e)
            except ValueError:
                f1 = False
                break
            else:
                f1 = True
    #条件2：
    initial = line_list[0]
    if initial.isupper():
        f2 = True
    elif initial.islower():
        f2 = True
    else:
        f2 = False
        
    #条件3
    ifup = False
    iflow = False
    ifint = False
    for e in line_list:
        if e.isupper():
            ifup = True
        elif e.islower():
            iflow = True
        else:
            try:
                int(e)
            except ValueError:
                pass
            else:
                ifint = True
    f3_list = [ifup,iflow,ifint]
    if f3_list.count(True) >= 2:
        f3 = True
    else:
        f3 = False
    #条件4
    if len(line_list) >= 8:
        f4 = True
    else:
        f4 = False
    #最终判断
    if f1 and f2 and f3 and f4:
        results.append('YES')
    else:
        results.append('NO')

for r in results:
    print(r)
