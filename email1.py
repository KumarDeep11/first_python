
a=input("Enter your email: ")

if len(a) >=10 and a.count(' ')==0 :#1
    if a[0].isalpha() and a.islower() and a.count('#')==0 and a.count('&')==0 and a.count('*')==0 and a.count('(')==0 :#2
     if ('@' and '.com'  in a) and (a.isalnum() or a.count('@')==1 and a.count('.')<=3) and a.count(',')==0 and a.count('{')==0:#3
        if a[-7]=='.' or a[-4]=='.' and a.count('!')==0 and a.count('|')==0 and a.count('/')==0 and a.count('-')==0:#4
         if (a[-2]=='i' and a[-1]=='n') or (a[-1]=='m' and a[-2]=='o' and a[-3]=='c'):#5
            
              print("Right email:")
         else: 
          print("Wrong email:")
        else:  
         print("Wrong email:")
     else: 
      print("Wrong email:")

    else: 
     print("Wrong email:")
 
else:
    print("Wrong email:")
