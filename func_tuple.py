def avg(*num):
    sum=0 
    for i in num:
        sum=sum+i
    print("Average of the numbers is:", sum/len(num))

avg(9,8,9,10)