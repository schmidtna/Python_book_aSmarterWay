# name = input("Type your name: ")
# print("Hello,", name)

# age = input("Type your age: ")
# print("Next year you will be", int(age) + 1)

# pi_value = 3.14
# circ_radi = 10
# print(pi_value * (circ_radi ** 2))

# base_rect = 10
# height_rect = 2
# print(base_rect * height_rect)
# base_rect = 6
# print(base_rect * height_rect)

name = "Nick"
first = name
age = 1000
print(id(age))
age = age + 1
print(id(age))
names = []
print(id(names))
names.append("Churro")
print(id(names))