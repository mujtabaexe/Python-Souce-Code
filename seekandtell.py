with open("file.txt", "w") as f:
    line=("Hello my name is Sahibzada Ahmad Mujtaba")
    f.writelines(line)
    print(type(f))
    
with open("file.txt", "r") as f:
    f.seek(17)
    data=f.read()
    print(data)

