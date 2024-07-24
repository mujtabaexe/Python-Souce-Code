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

print(dic.keys(),"\n") # Prints the keys 

for key in dic.keys():
    print(dic[key]) # Print the values of the keys                   
print()
for key in dic.keys():
    print(f"The value corresponding to the key {key} is {dic[key]}")
print()
for key in dic.keys():
    print(f"The value corresponding to the key {key} is {dic.keys()}") # Just to check 
print()