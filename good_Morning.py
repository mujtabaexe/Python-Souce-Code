import time
timestamp = time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))
print(hour)
if (hour>0 and hour<12):
    print("Good Morning Sir!")
elif (hour>= 12 and hour<19):
    print("Good Afternoon Sir!")
elif (hour>=19 and hour<0):
    print("Good Night Sir!")
