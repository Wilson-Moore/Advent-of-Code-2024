#include <stdio.h>
#include <stdlib.h>

void init(int A[],int size)
{
    for (size_t i = 0; i < size; i++)
    {
        A[i]=0;
    }
}

int Partition(int A[],int low,int high)
{
    int pivot=A[high];
    int tmp,i=low-1;
    for (int j = low; j < high; j++)
    {
        if(A[j]<=pivot)
        {
            i++;
            tmp=A[i];
            A[i]=A[j];
            A[j]=tmp;  
        }
    }
    tmp=A[i+1];
    A[i+1]=A[high];
    A[high]=tmp;
    return i+1;
} 

void Quick_Sort(int A[],int low,int high)
{
    if (low<high)
    {
        int part=Partition(A,low,high);
        Quick_Sort(A,low,part-1);
        Quick_Sort(A,part+1,high);
    }
}

int Similarity(int A[],int B[],int size)
{
    int sum=0;
    for (size_t i = 0; i < size; i++)
    {
        int j=i;
        int sim=0;
        for (size_t j = 0; j < size; j++)
        {
            if (A[i]==B[j])
            {
                sim++;
            }
        }
        sum=sum+A[i]*sim;
    }
    return sum;
}

int main(int argc, char const *argv[])
{
    if (argc < 2)
    {
        printf("Wrong format try:'solution_2 <filename.txt>'");
        exit(0);
    }
    
    FILE *fp=fopen(argv[1],"r");
    char buffer[8];
    int col=1,index=0;
    int A[1000],B[1000];
    init(A,sizeof(A)/sizeof(A[0]));
    init(B,sizeof(B)/sizeof(B[0]));

    while (fgets(buffer,8,fp))
    {
        if (col==1)
        {
            A[index]=atoi(buffer);
            col=2;
        }
        else if (col==2)
        {
            B[index]=atoi(buffer);
            col=1;
            index++;
        }
    }
    
    Quick_Sort(A,0,sizeof(A)/sizeof(A[0])-1);
    Quick_Sort(B,0,sizeof(B)/sizeof(B[0])-1);
    printf("%d",Similarity(A,B,sizeof(A)/sizeof(A[0])));

    fclose(fp);
    return 0;
}