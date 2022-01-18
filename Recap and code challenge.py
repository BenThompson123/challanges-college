print('Enter correct username and password combo to continue')
count = 0


password = ""
username = ""


while password!='password' and username!='ben' and count < 3:
    
    username = input("Enter username: ")
    password = input("Enter password: ") 

    if password=='password' and username=='ben':
     
     print('Access granted')
     break

    else:
        print('Access denied. Try again.')
        count+=1

while True:
    print("""
        1.Power tools
        2.Power tool accessories
        3.Hand tools
        4.Tool storage
        5.Measuring tools
        6.Testing equipment
        7.Heating & plumbing
        8.electrical & lighting and screws
        nails & fixings
        0.Search
        """)
    ans=input ("What would you like to buy ")
    if ans=="1":
        item1 = print("""
            A.Drill £24.99         1234567  8
            B.Sanding belt £199.99 2345678  1
            C.Circular Saw £199.99 3456789  3
            D.Exit
            """)
        item1=input ("Which power tool would you like to buy ")
        if item1=="A":
            print ("You have succefully purchased a Drill")
        elif item1=="B":
                print ("You have succefully purchased a Sanding belt")
        elif item1=="C":
                print ("You have succefully purchased a Circular Saw")
        elif item1=="D":
                break
    elif ans=="2":
        print("""
            A.Drill bit                   £24.99         0467890  8
            B.Sanding belt 12 grain belt  £199.99        2345678  1
            C.Circular Saw blade          £199.99        3456789  3
            D.Exit
            """)
        ans=input ("Which power tool accessories would you like to buy ")
        if ans=="A":
                print ("You have succefully purchased a Drill")
        elif ans=="B":
                print ("You have succefully purchased a Sanding belt")
        elif ans=="C":
                print ("You have succefully purchased a Circular Saw blade")
        elif ans=="D":
            break
    elif ans=="3":
        print("""
            A.Wrench                      £24.99         0467890  8
            B.Screwdriver                 £199.99        2345678  1
            C.Hammer                      £199.99        3456789  3
            D.Exit
            """)
        ans=input ("Which power tool accessories would you like to buy ")
        if ans=="A":
                print ("You have succefully purchased a Wrench")
        elif ans=="B":
                print ("You have succefully purchased a Screwdriver")
        elif ans=="C":
                print ("You have succefully purchased a Hammer")
        elif ans=="D":
            break
    elif ans=="4":
        print("""
            A.Tool box                    £24.99         0467890  8
            B.Tool drawer                 £199.99        2345678  1
            C.Tool cupboard               £199.99        3456789  3
            D.Exit
            """)
        ans=input ("Which power tool accessories would you like to buy ")
        if ans=="A":
                print ("You have succefully purchased a Tool box")
        elif ans=="B":
                print ("You have succefully purchased a Tool drawer")
        elif ans=="C":
                print ("You have succefully purchased a Tool cupboard")
        elif ans=="D":
            break
    elif ans=="5":
        print("""
            A.Ruler                      £24.99         0467890  8
            B.level checker              £199.99        2345678  1
            C.Tape measure               £199.99        3456789  3
            D.Exit
            """)
        ans=input ("Which power tool accessories would you like to buy ")
        if ans=="A":
                print ("You have succefully purchased a Ruler")
        elif ans=="B":
                print ("You have succefully purchased a Level Checker")
        elif ans=="C":
                print ("You have succefully purchased a Tape measure")
        elif ans=="D":
            break
    elif ans=="6":
        print("""
            A.Circuit detector           £24.99         0467890  8
            B.Metal detector             £199.99        2345678  1
            C.Motion detector            £199.99        3456789  3
            D.Exit
            """)
        ans=input ("Which power tool accessories would you like to buy ")
        if ans=="A":
                print ("You have succefully purchased a Circuit detector")
        elif ans=="B":
                print ("You have succefully purchased a Metal detector")
        elif ans=="C":
                print ("You have succefully purchased a Motion detector")
        elif ans=="D":
            break
    elif ans=="7":
        print("""
            A.Plunger                    £24.99         0467890  8
            B.Thermometor                £199.99        2345678  1
            C.U bend pipe                £199.99        3456789  3
            D.Exit
            """)
        ans=input ("Which power tool accessories would you like to buy ")
        if ans=="A":
                print ("You have succefully purchased a Plunger")
        elif ans=="B":
                print ("You have succefully purchased a Thermometor")
        elif ans=="C":
                print ("You have succefully purchased a U bend pipe")
        elif ans=="D":
            break
    elif ans=="8":
        print("""
            A.Wires                       £24.99         0467890  8
            B.Square light                £199.99        2345678  1
            C.3 inch screw                £199.99        3456789  3
            D.Exit
            """)
        ans=input ("Which power tool accessories would you like to buy ")
        if ans=="A":
                print ("You have succefully purchased a Wires")
        elif ans=="B":
                print ("You have succefully purchased a Square light")
        elif ans=="C":
                print ("You have succefully purchased a 3 inch screw")
        elif ans=="D":
            break
        elif ans=="0":
            print ("what would you like to search for")
            def find_index(elements, value):
                for index, element in enumerate(elements):
                    if element == value:
                        return index


        
      
   
