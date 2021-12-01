# log in sign up :-                                                                                                                                                                                     import json
import os
main_dict={}
list=[]
dict_out={}
user_info={}
if os.path.exists("userdetails.json"):
    with open("userdetails.json","r") as file:
        userdata=json.load(file)
else:
    f = open("userdetails.json","w")

choose=int(input("choose 1 for signing in\nchoose 2 for logging in\nchoose 3 for exit:"))
if choose==1:
    name=input("Enter your First name")
    last_name=input("Enter last name")
    for i in userdata["user"]:
        # print(i)
        if name == i["username"]:
             print("exist")
             break
    else:
        print(name+last_name)
        password=input("Enter your password:Password should contain:-\n1).upper and lower letters,\n2).It should contain at least one special character\n3).at least one numbers also")
        upper,lower,digit,special=0,0,0,0
        for i in password:
            if i.isupper():
                upper+=1
            if i.islower():
                lower+=1
            if i.isdigit():
                digit+=1
            if (i=="@" or i=="#" or i=="$" or i=="_" ):
                special+=1
        try:
            with open("userdetails.json","r") as output:
                data=json.load(output)
                for info in data["user"]:
                    pass
        except:
            pass
        if lower>=1 and upper>=1 and special>=1 and digit>=1 and lower+upper+special+digit==len(password):
            confirm_password=input("Enter your password to confirm")
            if password==confirm_password:
                # if os.stat("userdetails.json").st_size==0:
                    print("Congratulations!",name,"your profile has been created successfully!")
                    description=input("Write about yourself")
                    dob=input("enter your date of birth")
                    gender=input("enter gender")
                    hobbies=input("enter your hobbies")
                    user_info["description"]=description
                    user_info["DOB"]=dob
                    user_info["Gender"]=gender
                    user_info["hobbies"]=hobbies
                    dict_out["username"]=name
                    dict_out["Password"]=password
                    dict_out["Profile"]=user_info
                    list.append(dict_out)
                    main_dict["user"]=list
                    with open("userdetails.json","r") as file:
                        userdata=json.load(file)
                    for j in userdata:
                        if j=="user":
                            x=userdata[j]
                            x.append(dict_out.copy())
                            main_dict["user"]=x
                            print(main_dict)    
                            with open("userdetails.json","w")as f:
                                f.write(json.dumps(main_dict,indent=4))
                    
                    # else:
                        # print("Your account already exists!")
            else:
                print("Your Password has not been matched")
        else:
            print("Your password is invelid something missing in your password")

elif choose==2:
    name=input("enter your username")
    for i in userdata["user"]:
        if name == i["username"]:
            password=input("enter your Log in Password=")
            with open("userdetails.json","r") as log_in_file:
                log_in_info=json.load(log_in_file)
                for output_data in log_in_info["user"]:
                    if output_data["username"] == name and output_data["Password"]==password:
                        print(name+ "You  are Logged in Succesfully")
                        print("--------------------")
                        print("       PROFILE       ")
                        print("--------------------")
                        print("username",":",output_data["username"])
                        print("Gender",":",output_data["Profile"]["Gender"])
                        print("Bio",":",output_data["Profile"]["description"])
                        print("Dob",":",output_data["Profile"]["DOB"])
                        print("hobies",":",output_data["Profile"]["hobbies"])
                        break
                else:
                    print("Password and username are Invalid")        
    else:
        if name != i["username"]:
            print("This Account Doesn't Exist sign in please")