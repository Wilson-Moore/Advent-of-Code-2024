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

def make_list(level):
    big_list=[]
    for i in range(0,len(level)):
        small_lest=[]
        for j in range(0,len(level)):
            if j!=i:
                small_lest.append(level[j])
        big_list.append(small_lest)
        
    return big_list

def Dampener(sub_levels):
    for level in sub_levels:
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
            return 1
    return 0
    

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
        if safe==0:
            sub_levels=make_list(level)
            safe=Dampener(sub_levels)
        if safe==1:
            sum+=1
    return sum
            
print(Safe_Floors(Read_File()))