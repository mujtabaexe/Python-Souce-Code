### NOW A MORE BETTER WAY TO MAKE CLASS OTHER THAN CLASS AND OBJECT FILE METHOD IS  ...  USING __init__() --> DUNDER METHOD

### JUST BASIC 
def greet(fx):
    def mfx(*args,**kwargs):
        print("Hello")
        fx(*args,**kwargs)
        print("Thanks for using this function")
    return mfx


class Person:
    def __init__(self, name,occ):
        self.name=name
        self.occ=occ
        
    @greet
    def info(self):
        print(f"{self.name} is a {self.occ}")


a=Person("Mujtaba", "Developer")
a.info()


### CREATED A PROGRAM

# class Person:
#     def __init__(self, name,occ):
#         self.name=[]
#         self.occ=[]
#         while True:
#             n=input("Enter Name or \"exit\" to exit: ")
#             if n.lower()==("exit"):
#                 break
#             o=input("Enter occupation: ")
#             self.name.append(n)
#             self.occ.append(o)
        
#     def info(self):
#         for n, o in zip(self.name, self.occ):    
#             print(f"{n} is a {o}")
        
# a=Person("Mujtaba", "Developer")
# a.info()


### GPT PROGRAM

# class Person:
#     def __init__(self):
#         self.people = []

#         while True:
#             name = input("Enter Name or 'exit' to exit: ")
#             if name.lower() == "exit":
#                 break
#             occ = input("Enter occupation: ")
#             self.people.append((name, occ))

#     def info(self):
#         for name, occ in self.people:
#             print(f"{name} is a {occ}")

# a = Person()
# a.info()
