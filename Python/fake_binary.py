def fake_bin(x):
    
    newList = []

    for i in x:
        i = int(i)
        if i < 5:
            newList.append(0)
        
        elif i >= 5:
            newList.append(1)


    my_str = ''.join(map(str, newList))
    return my_str
