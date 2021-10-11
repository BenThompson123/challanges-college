import array as arr
a = arr.array('i', [2, 4, 6, 8, 10, 12, 12])

reversed = input("hello if you want the array to be reversed type 1 if not type nothing")

if(reversed == ""):


  print("First element:", a[1])
  print("Second element:", a[2])
  print("Third element:", a[3])
  print("Fourth element:", a[-3])
  print("Fifth element:", a[-2])
  print("Last element:", a[-1])
  print("Last element:", a[-1])


if(reversed == "1"):
     print("Last element:", a[-1])
     print("Last element:", a[-1])
     print("Fifth element:", a[-2])
     print("Fourth element:", a[-3])
     print("Third element:", a[3])
     print("Second element:", a[2])
     print("First element:", a[1])
     
from array import *
array_num = array("i", [2, 4, 6, 8, 10, 12, 12])
print("Original array: "+str(array_num))
print("Number of occurence of the number 12 in the array: "+str(array_num.count(12)))

element = int(input("which element do wanna remove "))
from array import *
array_num = array('i', [2, 4, 6, 8, 10, 12, 12])
print("Original array: "+str(array_num))
print("Remove the desired item form the array:")
array_num.pop(element)
print("New array: "+str(array_num))

from array import *
array_num = array('i', [2, 4, 6, 8, 10, 12, 12])
print("Original array: "+str(array_num))
print("Current memory address and the length in elements of the buffer: "+str(array_num.buffer_info()))
print("The size of the memory buffer in bytes: "+str(array_num.buffer_info()[1] * array_num.itemsize))
