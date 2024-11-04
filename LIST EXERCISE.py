#Creating a List
fruits=['apple','banana','grapes','orange','kiwi']
print(fruits)
#Accessing Elements
colors = ['red', 'blue', 'green', 'yellow', 'purple']
print(colors[0])
print(colors[2])
print(colors[4])
#Modifying a List
numbers=[10, 20, 30, 40, 50]
numbers[1]=25
numbers.append(60)
print(numbers)
#List Slicing
names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma']
subset = names[:3]
print(subset)
#Looping through a List
numbers = list(range(1, 11))
for num in numbers:
    print(num ** 2)
#List Methods: Append and Extend
shopping_cart = []
shopping_cart.append('milk')
shopping_cart.append('bread')
shopping_cart.append('eggs')
shopping_cart.extend(['butter', 'cheese'])
print(shopping_cart)
#Finding Maximum and Minimum in a List
numbers = [45, 22, 88, 56, 92, 33]
max=max(numbers)
min=min(numbers)
print(max)
print(min)
#Counting Occurrences
letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
a= letters.count('a')
print(a)
#List Comprehension
square = [x**2 for x in range(11) if x % 2 == 0]
print(square)
#Removing Duplicates
nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
Num = list(set(nums))
print(Num)

