# for i in range(1, 11):
#     print(i)


# for i in range(2, 21, 2):
#     print(i)


# total = 0

# for i in range(1, 101):
#     total += i

# print("Sum =", total)


# num = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)


# num = int(input("Enter a number: "))
# count = 0

# while num > 0:
#     num = num // 10
#     count += 1

# print("Digits:", count)


# num = int(input("Enter a number: "))
# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# print("Reversed number:", reverse)


# num = int(input("Enter a number: "))
# isPrime = True

# if num <= 1:
#     isPrime = False
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             isPrime = False
#             break

# if isPrime:
#     print("Prime")
# else:
#     print("Not Prime")


# num = int(input("Enter a number: "))
# factorial = 1

# for i in range(1, num + 1):
#     factorial *= i

# print("Factorial =", factorial)


# rows = int(input("Enter number of rows: "))

# for i in range(1, rows + 1):
#     print("*" * i)


# secret = 7
# guess = 0

# while guess != secret:
#     guess = int(input("Guess the number: "))

#     if guess == secret:
#         print("Correct!")
#     else:
#         print("Try again.")
