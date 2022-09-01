import re
a="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{3,3}$"
b=input("Enter a mail: ")
if re.search(a,b):
    print("Right mail")
else:
    print("Wrong mail")
