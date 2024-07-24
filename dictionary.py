dic={ 0 : "Sahibzada",
     1: "Ahmad",
     2:"Mujtaba",
     "emp": "emp_Zeeshan"}
print(dic[0])
print(dic[1])
print(dic[2])
print(dic.get("emp2)"),"\n") # It will print none
# print(dic["emp2"])# It will throw an error
print(dic["emp"],"\n") 

print(dic.keys(),"\n")

for key in dic.keys():
    print(dic[key])