#number = int(input("Enter a number: "))
#
#if number % 3 == 0 and number % 5 == 0:
#    print("Divisible by both 3 and 5")
#elif number % 3 == 0:
#    print("Divisible by 3 only")
#elif number % 5 == 0:
#    print("Divisible by 5 only")
#else:
#    print("Not divisible by 3 or 5")


#year = int(input("Enter a year: "))
#
#if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#    print("Leap year")
#else:
#    print("Not a leap year")


#purchase = float(input("Enter purchase amount: "))
#
#if purchase >= 1000:
#    discount = purchase * 0.20
#elif purchase >= 500:
#    discount = purchase * 0.10
#else:
#    discount = 0
#
#final_amount = purchase - discount
#
#print("Discount:", discount)
#print("Final amount:", final_amount)


#score1 = float(input("Enter score 1: "))
#score2 = float(input("Enter score 2: "))
#score3 = float(input("Enter score 3: "))
#
#average = (score1 + score2 + score3) / 3
#
#if average >= 90:
#    grade = "A"
#elif average >= 80:
#    grade = "B"
#elif average >= 75:
#    grade = "C"
#else:
#    grade = "Failed"
#
#print("Average:", average)
#print("Grade:", grade)


#num1 = int(input("Enter first number: "))
#num2 = int(input("Enter second number: "))
#num3 = int(input("Enter third number: "))
#
#if num1 >= num2 and num1 >= num3:
#    largest = num1
#elif num2 >= num1 and num2 >= num3:
#    largest = num2
#else:
#    largest = num3
#
#print("Largest number is:", largest)


#age = int(input("Enter your age: "))
#citizen = input("Are you a citizen? (yes/no): ").lower()
#
#if age >= 18 and citizen == "yes":
#    print("Eligible to vote")
#else:
#    print("Not eligible to vote")


#salary = float(input("Enter monthly salary: "))
#years = int(input("Years of service: "))
#
#if salary >= 30000 and years >= 5:
#    print("Qualified for bonus")
#else:
#    print("Not qualified for bonus")


#username = input("Username: ")
#password = input("Password: ")
#
#if username == "admin":
#    if password == "python123":
#        print("Access granted")
#    else:
#        print("Wrong password")
#else:
#    print("Username not found")


#side1 = float(input("Enter side 1: "))
#side2 = float(input("Enter side 2: "))
#side3 = float(input("Enter side 3: "))
#
#if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
#    if side1 == side2 == side3:
#        print("Equilateral Triangle")
#    elif side1 == side2 or side2 == side3 or side1 == side3:
#        print("Isosceles Triangle")
#    else:
#        print("Scalene Triangle")
#else:
#    print("Invalid Triangle")


#hour = int(input("Enter hour (0-23): "))
#
#if 5 <= hour <= 11:
#    print("Good Morning")
#elif 12 <= hour <= 17:
#    print("Good Afternoon")
#elif 18 <= hour <= 21:
#    print("Good Evening")
#elif 0 <= hour <= 23:
#    print("Good Night")
#else:
#    print("Invalid hour")
