#wap to calculate the grade of a students from his marks from the following scheme
# 10-30-C
# 30-50-B
# 50-70-A 
# 70-100-EX 
marks = int(input("enter your marks:"))
if( marks<=100 and marks >= 70):
    grade="ex"
elif( marks<=70 and marks>=50):
    grade="A"
elif( marks<=50 and marks>=30):
    grade="B"
elif( marks<=30 and marks>=10):
    grade="C"
    print("your grade is:","grade")
