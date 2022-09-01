a=input("Enter your mobile number +91-")
if a.isdigit() and len(a)==10:
    if a[0]=="9" or a[0]=="8" or a[0]=="7" or a[0]=="6":
     print("Valid Number")
    else:
        print("Not a valid number")
else:
    print("Not a valid number")