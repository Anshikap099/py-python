#creat an empty dictonary allow 4 friends to enter their favorite language as value and use key as their names.and names should be unique 
d ={}
name = input("enter friends name:")
lang = input("enter language name :")
d.update({name:lang})
name = input("enter friends name:")
lang = input("enter language name :")
d.update({name:lang})
name = input("enter friends name:")
lang = input("enter language name :")
d.update({name:lang})
name = input("enter friends name:")
lang = input("enter language name :")
d.update({name:lang})
print(d)
# if the names are same
# then it will updated 