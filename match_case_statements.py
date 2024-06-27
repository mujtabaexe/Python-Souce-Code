a=int(input("Enter a: "))
match a:
    case 0:
        print("a is zero")

    case 4:
        print("a is 4")
    
    case _ if a!=90:
        print("a is not 90")
    case _ if a!=80:
        print("a is not 80")
    
    case _:
        print(a)




print("\nif else ...................................................\n")

if a==0:
        print("a is zero")

elif a==4:
        print("a is 4")
    
elif a!=90:
        print("a is not 90")
elif a!=80:
        print("a is not 80")
    
else:
        print(a)


print("\nonly ifs  ...................................................\n")

if a==0:
        print("a is zero")

if a==4:
        print("a is 4")
    
if a!=90:
        print("a is not 90")
if a!=80:
        print("a is not 80")
    
else:
        print(a)