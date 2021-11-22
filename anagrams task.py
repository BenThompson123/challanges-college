def areAnagram(str1, str2):
    #this would get the length of both of the strings
    n1 = len(str1)
    n2 = len(str2)

    #this if for when they aren't the same length
    if n1 != n2:
        return 0

    #This will sort both the strings
    str1 = sorted(str1)
    str2 = sorted(str2)

    #This will sort the strings
    for i in range(0, n1):
        if str1[i] != str2[i]:
            return 0

    return 1
    

#this is a driver code
str1 = input("Enter a word to check if its an angaram ")
str2 = input("Enter a word to check if its an angaram ")

#this is a function call
if areAnagram(str1, str2):
        print("These two are anagrams of eachother")
else:
        print("These aren't anagrams of eachother")
