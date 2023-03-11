import random

min_num = int(input("Enter the minimum number. "))
max_num = int(input("Enter the maximum number. "))

random_num = random.randint(min_num, max_num)

print("The random number between:", min_num, "and", max_num, "is:", random_num)
