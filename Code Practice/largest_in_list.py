list=[2,3,6,5,7,8,9,10,11,12,13,14,15]
largest = 0;
for number in list:
    if number > largest:
        largest = number
print(f"The largest number in the list is: {largest}")