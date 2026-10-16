#Program developed by Sam Espana (textbook - Figure 67)

print("Displaying for loops with range (single value)\n")
for index1 in range(4):
    print("Python for loop with range of single value. Index =", index1)
index1 = 0
print("\nPython while loop with index 1 value. Index =", index1)
print()
while (index1 < 4):
    print("Index1 =", index1)
    index1 += 1

print("\nPython for loop with two parameters (1,5) \n")
for index2 in range(1,5):
    print("Index =", index2)

#while loop below

print("\nPython while loop with two parameters (1,5) \n")
index2 = 1
while (index2 < 5):
    print("Index2 =", index2)
    index2 += 1
    
print("\nTimes table for #X using for loop \n")
intNumber = int(input("Enter integer number for table > 0 : "))
intLowerBound = 1
intUpperBound = 10
for index3 in range(intLowerBound, intUpperBound+1):
    print(intNumber, "x", index3, "=", intNumber*index3)

#while loop below

print("\nTimes table for #X using while loop \n")
intNumber2 = int(input("Enter integer number for table > 0: "))
index3 = 1
while (index3 < intUpperBound+1):
    print(intNumber2, "x", index3, "=", intNumber2*index3)
    index3 += 1

print("\nBlong Lor")
