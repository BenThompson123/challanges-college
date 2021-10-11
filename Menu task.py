print('Enter correct username and password combo to continue')
count = 0


password = ""
username = ""


while password!='Password' and username!='ben' and count < 3:
    
    username = input("Enter username: ")
    password = input("Enter password: ")

    if password=='Password' and username=='ben':
     
     print('Access granted')
     break

    else:
        print('Access denied. Try again.')
        count+=1       
print ("""
    1.Add a item
    2.View all the items
    3.remove an item
    0.Exit
    """)
ans=input ("what would you like to do ")
if ans=="1":
        item1 = input ("what do you wanna call said item")
        print (item1+" has been sucefully added")
elif ans=="2": 
      print ("these are all the existing files as of current")
      print ("""
            Hello
            Hi
            Yalright
            """)
elif ans=="3":
    print ("these are all the existing files as of current")
    print ("""
            1.hello
            2.hi
            3.yalright
            """)

    file = input (" which of the files would you like to be removed ")
    if file == "1":
        print ("these are all the existing files as of current")
        print ("""
                    2.Hi
                    3.Yalright
                    """)
        
    elif file == "2":
            print ("these are all the existing files as of current")
    print ("""
            1.hello
            3.yalright
            """)
    if file == "3":
            print ("these are all the existing files as of current")
    print ("""
            1.hello
            2.hi
            """)

elif ans== "0":
        finish = input("Alright see you later then")

            



    
      
            
    
