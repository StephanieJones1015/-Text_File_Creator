name = input("What's your name? \n")
color = input("What is your favorite color? ")
with open('example.txt', 'w') as file:
    file.write(f"{name} created this file")
    file.write(f"{color}\n")