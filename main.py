# Using break to find the first even number in a list
numbers = [1, 3, 5, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print("Found the first even number:", num)
        break


 # Using continue to print only odd numbers in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for num in numbers:
            if num % 2 == 0:
                continue
            print("Odd number:", num)