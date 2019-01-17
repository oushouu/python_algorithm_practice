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
