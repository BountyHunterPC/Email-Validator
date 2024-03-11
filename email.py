email = input("Enter your e-mail: ") #a@a.in pranav123@gmail.com
spaceflag, upperflag, specialsymbolflag = 0, 0, 0
extension = email.split("@")
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if ((email[-4]==".") ^ (email[-3]==".")):
                for index, char in enumerate(email):
                    if char == char.isspace():
                        spaceflag = 1
                    elif char.isalpha():
                        if char == char.upper():
                            upperflag = 1
                    elif (email[index] == ".") and (email[index-1] == "."):
                        print("Consecutive . are not allowed!")
                    elif (email[index] == "@" and (email[index+1] == ".")) or (email[index] == "." and (email[index+1] == "@")):
                        print(". immediately followed by @ and vice-versa not allowed!")
                    elif char.isdigit():
                        continue
                    elif char == "_" or char == "." or char == "@":
                        continue
                    else:
                        specialsymbolflag = 1     
                if spaceflag == 1 or upperflag == 1 or specialsymbolflag == 1:
                    print("Spaces , Uppercase, Special characters are not allowed!")         
            else:
                print("Please use right extension")
        else:
            print("@ not included or More than one @ are not allowed!")
    else:
        print("Email should not start with a digit!")
else:
    print("Email length can't be less than 6!")


