def EX7():
    x = input("Adj meg egy mondatot:")
    l = []
    for i in x.split(' '):
        if i == i[::-1]:
            l.append(i)
    min = 0
    for j in l:
        if len(j)>min:
            a = j
    return a

print(EX7())
