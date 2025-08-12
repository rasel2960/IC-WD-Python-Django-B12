"""
5-6. Stages of Life: Write an if-elif- else chain that determines a person’s stage
of life. Set a value for the variable age, and then:•
- If the person is less than 2 years old, print a message that the person is
a baby.•
- If the person is at least 2 years old but less than 4, print a message that the
person is a toddler.•
- If the person is at least 4 years old but less than 13, print a message that
the person is a kid.•
- If the person is at least 13 years old but less than 20, print a message that
the person is a teenager.•
- If the person is at least 20 years old but less than 65, print a message that
the person is an adult.•
- If the person is age 65 or older, print a message that the person is an elder.
"""
print("Enter your age:")
age = int(input("> "))

if age < 2:
    print(f"You are a baby. Your current age is {age}.")
elif age >=2 and age < 4:
    print(f"You are a toddler. Your current age is {age}.")
elif age >=4 and age < 13:
    print(f"You are a kid. Your current age is {age}.")
elif age >=13 and age < 20:
    print(f"You are a teenager. Your current age is {age}.")
elif age >= 20 and age < 65:
    print(f"You are an adult. Your current age is {age}.")
elif age >= 65:
    print(f"You are an elder. Your current age is {age}.")
