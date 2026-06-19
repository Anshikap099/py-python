#fake message detection
p1=" make a lot of money "
p2="buy now"
message = input("enter your commnet :")
if(("p1 in a message")or ("p2 in a message")):
    print("this comment is spam")
else:
    print("this comment is not a spam")