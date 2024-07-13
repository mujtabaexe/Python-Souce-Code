# def avg(*num):
#     sum=0 
#     for i in num:
#         sum=sum+i
#     print("Average of the numbers is:", sum/len(num))

# avg(9,8,9,10)


tup=(1,"Hello",True,232,55,999)
print(type(tup),tup)
print(tup[4])

print(tup[-3])

tup2=tup[:4] #New tuple is created


temp=list(tup)
while True:
    a=input("Enter: ")
    if a=="exit":
        break
    temp.append(a)
print(temp,"TEMP\n\n")

tup=tuple(temp)

print(tup,"Converted to tuple again")

# Converted to tuple now and cannot be changed because tuple cannnot be changed
while True:
    a=input("Enter: ")
    if a=="exit":
        break
    tup.append(a)

print(tup)