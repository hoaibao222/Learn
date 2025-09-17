# This game is absolutely unfair
your_name = input("Enter your name here: ")
name_value = 0

for i in range(0, len(your_name)):
    specific_value = ord(your_name[i])
    if specific_value != 32:
        name_value += specific_value

print(name_value)
