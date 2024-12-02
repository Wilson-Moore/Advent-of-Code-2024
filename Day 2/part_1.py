def Read_File():
    f=open("./day 2/input.txt","r")
    buffer=f.readline()
    levels=[]
    while buffer:
        str_list=buffer.split(" ")
        int_list=[]
        for var in str_list:
            int_list.append(int(var))
        levels.append(int_list)
        buffer=f.readline()
    return levels

def Safe_Floors(levels):
    sum=0
    for level in levels:
        safe=1
        sign=level[0]-level[1]
        for i in range(0,len(level)-1):
            if sign>0:
                if level[i]==level[i+1] or abs(level[i]-level[i+1])>3 or level[i]-level[i+1]<0:
                    safe=0
            else:
                if level[i]==level[i+1] or abs(level[i]-level[i+1])>3 or level[i]-level[i+1]>0:
                    safe=0
        if safe==1:
            sum+=1
    return sum
            
print(Safe_Floors(Read_File()))