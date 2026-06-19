#write a programme to enter the greatest of  4 nuumbers entered by user
a1=int(input("enter numbre 1:"))
a2=int(input("enter numbre 2:"))
a3=int(input("enter numbre 3:"))
a4=int(input("enter numbre 4:"))

if(a1>a2 and a1>a3 and a1>a4):
    print("a is greatest number")
elif(a2>a1 and a2>a3 and a2>a4):
    print("a2 is the greatest number")
elif(a3>a1 and a3>a2 and a3>a4):
    print("a3 is the greatest number")
else:
    print("a4 is greatest number")
