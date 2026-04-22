#Create an algorithm to find the lowest value in a list:

myList = [90,3,56,123,67,87,56,90]

minVal = myList[0]
currPosition = 1
position = 0

for i in myList:
    if(i <=  minVal):
        minVal = i
        position = currPosition
    currPosition = currPosition + 1

print(f"Min Value: {minVal} at position: {position}")