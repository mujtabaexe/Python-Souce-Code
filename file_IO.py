# f=open("temp2.IO.txt","w") # makes a new file 
f = open("temp_IO.txt","a") # "r" mode is also a default
# print(f) #it prints the info of the text file not the inside mateerial
# text= f.read()
# print(text) # Now it will print its inside text also with the help of next line
# f.close


f = open ("my.txt","w")
lines =["line1","line2","Line3"]
for line in lines:
    f.writelines(line+"\n")
f.close()