# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
evenNumbers = [even for even in numbers if even %2 == 0]
print(evenNumbers)

# 2. Print the difference between the largest and smallest value:
largest = max(numbers)
smallest = min(numbers)
dif = largest - smallest
print(dif)

# 3. Print True if the list contains a 2 next to a 2 somewhere.

for index in range(len(numbers)):
    if numbers[index] == 2:
        if numbers[index-1] == 2 or numbers[index+1] == 2:
            print("True")
            break
        
# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
ignore = False
sum = 0
for index in range(len(numbers)):
    if numbers[index] == 6:
        ignore = True
    elif numbers[index] == 7:
        ignore = False
        continue
    if not ignore:
        sum += numbers[index]
print(sum)
     

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 
sum = 0
dontAddIndex = None
for index in range(len(numbers)):
    if numbers[index] == 13:
        dontAddIndex = index + 1
        continue
    if dontAddIndex != index:
        sum += numbers[index]

print(sum)






