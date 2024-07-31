class Employee:
    name=("Sahibzada Ahmad Mujtaba")
    occ= ("Software Engineer")
    networth= 10000

a=Employee()
c=Employee()
print(a,"\n") #  Prints the location in the memory
print(a.name)
print(a.occ)
print(a.networth)
print()

a.name="Wasey"
a.occ="Developer"
a.networth=15000

print(a.name, a.occ,a.networth)
print()

b=Employee()
b.name=("Hamdan")
b.occ=("Web Developer")
b.networth=16000
print(b.name, b.occ, b.networth)


print(Employee(),"------->Is the Address of the CLASS \n")
print(f"{a.name} is a {a.occ} and have a networth of {a.networth}")
print(f"{b.name} is a {b.occ} and have a networth of {b.networth}")
print(f"{c.name} is a {c.occ} and have a networth of {c.networth}")
print()

### WE CAN  ALSO MAKE A SELF 

class Person:
    name1=("Sahibzada Ahmad Mujtaba")
    occ1= ("Software Engineer")
    networth1= 10000

    def info(self):
        print(f"{self.name1} is a {self.occ1} and have a networth of {self.networth1}")
    
i=Person()
i.info()


b1=Person()
b1.name1=("Hamdan 1")
b1.occ1=("Web Developer 1")
b1.networth1=16000
b1.info()



