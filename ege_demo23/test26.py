with open('26.txt') as f:
    data=f.readlines()
    for i in range(len(data)):
        data[i]=int(data[i])
    print(data)
    answer=[]
    print(data)
