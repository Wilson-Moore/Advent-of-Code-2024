function Read_File()
    file=open("./day 3/input.txt","r")

    mul_list=[]
    for line in readlines(file)
       for i in eachindex(line)
        if line[i]=='m'&&line[i+1]=='u'&&line[i+2]=='l'&&line[i+3]=='('&&isdigit(line[i+4])
            first,second=0,0
            i+=4
            while isdigit(line[i])
                first=first*10+parse(Int,line[i])
                i+=1
            end
            if line[i]==','
                i+=1
                while isdigit(line[i])
                    second=second*10+parse(Int,line[i])
                    i+=1
                end
            end
            if line[i]==')'
                push!(mul_list,(first,second))
            end
        end
       end
    end
    return mul_list
end

function Multiply(list)
    sum=0
    for element in list
        sum=sum+element[1]*element[2]
    end
    return sum
end

list=Read_File()
sum=Multiply(list)