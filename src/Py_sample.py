'''
Created on May 21, 2017

@author: lthamby
'''
# stprint = input("Enter the favourite name:")
# print("Your " + stprint)
#from operator import index
#from _ast import Index

# NumbEnter= input("Enter Number to check:")
# NumbCheck=int(NumbEnter)
# if int(NumbCheck%2 == 0):
#     print("You have Entered"+ NumbEnter  +"is Even Number")
#     
# else:
#     print("You have Entered" + NumbEnter + "is Odd Number") 
    
enterList = [1,2,3,4,5,12,13,14,3]
ValCo = int(len(enterList)-1)

Nlist = []
for ValCo in range(0,len(enterList)):
    yok = int (enterList[ValCo]) - 5
    x = 0
    if yok < x:
     {
   
        Nlist.append(yok+5)  
     }
     
print(Nlist)

years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
ages = []
for year in years_of_birth: 
    ages.append(2014 - year)
print(ages)
  
#print(enterList[ValCo])
     



