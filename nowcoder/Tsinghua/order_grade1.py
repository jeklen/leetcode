while True:
    try:
        tol = input()
    except:
        break
    tag = input()
    items = []
    for i in range(tol):
        ss = input()
        items.append([ss.split()[0], int(ss.split()[1])])
        if tag:
            items = sorted(items, key=lambda x:x[1])
        else:
            items = sorted(items, key=lambda x:x[1], reverse=True)
        for it in items:
            print(it[0], it[1], end=' ')