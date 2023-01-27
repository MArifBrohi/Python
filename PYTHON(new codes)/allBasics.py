st = '''Muhammad arif
i study in sukkur university'''
print(st)

name = "ARIF"
print(name[0])
print("after using for loop: ")
for character in name:
    print(character)

print("these are typecasting: ")

num1 = "12"
num2 = "1"
print(num1+num2)

print(int(num1)+int(num2))
print(float(num1)+float(num2))

# HOW TO FIND THE LENGHT OF STRING
    # len() is a function which finds length

# lets try:
length = len("mango")
print("mango is",length,"character word!")

# TAKING INPUT FROM USER: LET'S TRY

name  = input("What is your name:")
print("My name is:",name)


# LET'S EXPLORE SOMETHING DIFFERENT
names = "Muhammad,Arif"
length = len(names)
print(length)

# DO YOU WANT TO PRINT JUST "MUHAMMAD", yes (THESE ARE CALLED SLICING)
print("Printing just",names[0:8]) # INCLUDING 0 BUT NOT 8

# WHAT ABOUT IF WE DON'T PUT 0 INDEX
print("Printing just",names[:8]) # PYTHON AUTO INITIALIZE 0 INDEX :)

na = "Arif"
print(na[-4:-2]) 
