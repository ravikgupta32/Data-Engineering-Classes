'''A data structure in Python is a specialized format for organizing,
 managing, storing, and processing data so that it can be accessed and 
 modified efficiently. Instead of keeping individual values in scattered 
 variables, data structures act as containers that group related information together.'''


#to define list we use []
myList =[1,2,'Ravi','Gupta',['aa','bb','vv']]
print(myList[0])
print(myList[4])
print(myList[0:3])
print(myList[-3:])

#Skip elements
print(myList[::3])
#Add element to the list
#Lists are mutuable -the value can be changed 
myList.append('Hero')
print(myList)
#Insert a data a particular place
myList.insert(1,'New')
print(myList)

#Delete a item
myList.pop() #Pop element from the end of the list
print(myList)