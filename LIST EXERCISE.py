fruits=['apple','banana','grapes','orange','kiwi']
print(fruits)
colors = ['red', 'blue', 'green', 'yellow', 'purple']
print(colors[0])
print(colors[2])
print(colors[4])
numbers=[10, 20, 30, 40, 50]
numbers[1]=25
numbers.append(60)
print(numbers)
names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma']
firstthree = names[:3]
print(firstthree)
numbers = list(range(1, 11))
for num in numbers:
    print(num ** 2)
shoppingcart = []
shoppingcart.append('milk')
shoppingcart.append('bread')
shoppingcart.append('eggs')
shoppingcart.extend(['butter', 'cheese'])
print(shoppingcart)
numbers = [45, 22, 88, 56, 92, 33]
max=max(numbers)
min=min(numbers)
print(max)
print(min)
letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
a= letters.count('a')
print(a)
square = [x**2 for x in range(11) if x % 2 == 0]
print(square)
nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
Num = list(set(nums))
print(Num)

