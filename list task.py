list = [1, 2, 3, 4, 5]

print (list)

list = ["one, two, three, four, five"]

print (list)

import array as arr
a = arr.array('i', [1,1, 2, 3, 4, 5])

reversed = input("hello if you want the array to be reversed type 1 if not type nothing ")

if(reversed == ""):


  print("First element:", a[1])
  print("Second element:", a[2])
  print("Third element:", a[3])
  print("Fourth element:", a[-2])
  print("Fifth element:", a[-1])
 

if(reversed == "1"):
     print("Last element:", a[-1])
     print("Fifth element:", a[-2])
     print("Third element:", a[3])
     print("Second element:", a[2])
     print("First element:", a[1])

combined = input("hello if you want to see a list and combined list type yes if not type nothing ")

if(combined == "yes"):
   list1 = [5,6,7,8,9]
   list2 = [10,11,12,13,14]
   combinedList = list1 + list2
   print(list1)
   print(list2)
   print(combinedList)

if(combined == ""):
  print("alright onto the next then")


numbers = [5, 6, 7, 8, 9]

squared_numbers = [number ** 2 for number in numbers]

print(squared_numbers)

