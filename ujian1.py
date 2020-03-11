#=========Soal Nomor 1=========#
# def Hashtag(word):
#     newWord = ''
#     hashtag = "#"
#     for i in word.split(' '):
#       newWord = newWord+i.capitalize()
#     if len(word) > 50:
#       print(False)
#     elif len(word) == 0:
#       print(False)
#     else: 
#       print(hashtag+newWord)

# Hashtag("Nama saya mike")

#=========Soal Nomor 2=========#
# def create_phone_number(number):
#   newNumber = []
#   first3 = ''
#   second3 = ''
#   lastNum = ''
#   for i in number:
#     newNumber.append(str(i))
#   for j in newNumber[0:3]:
#     first3 = first3+j 
#   for x in newNumber[3:6]:
#     second3 = second3+x
#   for l in newNumber[6:len(newNumber)]:
#     lastNum = lastNum+l
#   print("("+first3+") "+second3+"-"+lastNum)

# create_phone_number([1,2,3,4,5,6,7,8,9,0])

#=========Soal Nomor 3=========#
# def sort_odd_even(num):
#   newList = []
#   listGanjil = []
#   listGenap = []
#   for a in num:
#     if a %2 == 1:
#       listGanjil.append(a)
#     else:
#       listGenap.append(a)
  
#   #Ascending Ganjil
#   for i in range(len(listGanjil)):
#     for j in range(i + 1, len(listGanjil)):
#       if(listGanjil[i] > listGanjil[j]):
#         listGanjil [i], listGanjil[j] = listGanjil [j], listGanjil [i]
#       else:
#         pass
#   # print(listGanjil)

#   #Descending Genap
#   for i in range(len(listGenap)):
#     for j in range(i + 1, len(listGenap)):
#       if(listGenap[i] < listGenap[j]):
#         listGenap [i], listGenap[j] = listGenap [j], listGenap [i]
#       else:
#         pass
#   # print(listGenap)

#   newList = listGanjil + listGenap
#   print(newList)

# sort_odd_even([9,3,1,8,6,2])

#=========Soal Nomor 4=========#
# def hollow_triangle(number) : 
#   x = 0
#   for i in range(1,number) :
#     for j in range(i,number) : 
#       print('_', end='') 
          
#     while (x != (2 * i - 1)) : 
#         if (x == 0 or x == 2 * i - 2) : 
#             print('#', end='') 
#         else : 
#             print('_', end ='') 
#         x = x + 1
#     for k in range(i,number):
#       print('_', end='')
    
#     x = 0;
#     print () 
#   for i in range(0, 2 * number -1) : 
#       print ('#', end = '') 
#   print("\n") 

# hollow_triangle(4) 
 
  