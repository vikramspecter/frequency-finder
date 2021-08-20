a=input("enter the string for which you want to find the frequency")
def most_frequent(a):
    l=list(a)
    d={}
    for i in l:
        count=0
        for j in l:
            if i==j and count==0:
                count=1
            elif i==j and count!=0:
                count+=1
            d[i]=count
    return d
print("the frequency is",most_frequent(a))
