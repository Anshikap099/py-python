#wap to fing out wether a student has passed or fails if it requires a tutal of 40% and at least 30% in each subject to pass
#  assume 3 sub and takes marks as an input
marks1 =int(input("enter the marks 1 :"))
marks2 =int(input("enter the marks 2 :"))
marks3 =int(input("enter the marks 3 :")) 
# check foe total percentage
total_percentage = (100*( marks1+ marks2 +marks3))/300
if(total_percentage>=40):
   print("you are pass")

else:
    print("you are not pass,try again never give up")