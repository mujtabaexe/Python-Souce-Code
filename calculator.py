def calc(num1, num2, oper): 
    if oper == "+":
        print(f"num1 + num2 is = {num1 + num2}")
    elif oper == "-":
        print(f"num1 - num2 is ={num1-num2}")
    elif oper == "*":
        print(f"num1 * num2 is ={num1*num2}")
    elif oper == "/":
        while num2==0:
            print("num2 cannot be 0\n")
            num2=float(input("Enter num2 again: "))        
        print(f"num1/num2 is ={num1/num2}")
    

oper= input("Enter + to add , - to subtract, * to multipy , / to divide: ")
while oper not in  ["+","-","*","/"]:
    print("Invalid option please enter correct one: ")
    oper= input("Enter + to add , - to subtract, * to multipy , / to divide: ")

num1=float(input("Enter num1: "))
num2=float(input("Enter num2: "))

calc(num1,num2,oper)