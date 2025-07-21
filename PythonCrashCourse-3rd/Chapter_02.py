# Python Crash Course, 3rd Edition by Eric Matthes
# Chapter 2: Variables and Simple Data Types
# Try It Yourself

# 2-1. Simple Message: Assign a message to a varibale, and then print that message.
message = "Hello, Rasel! Welcome to Python Crash Course 3rd Edition by Eric Matthes."
print(message)

# 2-2. Simple Messages: Assign a new message to the variable, and print that message. Then change the value of the variable to a new message, and print the new message.
message2 = "I'm solving the exercises of Chapter 2 of Python Crash Course 3rd Edition by Eric Matthes."
print(message2)
message2 = "I'm learning about variables and simple data types in Python."

# 2-3. Personal Message: Use a variable to represent a person's name, and print a message to that person. Your message should be simple, such as "Hello Eric!" or "Would you like to learn some Python today?"
name = "Eric"
message3 = f"Hello {name}! Would you like to learn some Python today?"
print(message3)

# 2-4. Name Cases: Use a variable to represent a person's name, and then print that person's name in lowercase, uppercase, and title case.
name4 = "Rasel ahmed"
print(name4.lower())
print(name4.upper())
print(name4.title())

# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks:
# Albert Einstein once said, "A person who never made a mistake never tried anything new."
quote = 'Albert Einstein once said, "A person who never made a mistake never tried anything new."'
print(quote)

# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time represent the famous person's name using a variable called famous_person. Then compose your message and represent it with a new variable called message. Print your message.
famous_person = "Albert Einstein"
message4 = f"{famous_person} once said, \"A person who never made a mistake never tried anything new.\""
print(message4)

# 2-7. Stripping Names: Use a variable to represent a person's name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination "\t" and "\n" at least once. Print the name once, so that the whitespace surrounding the name is displayed. Then print the name using each of these functions: lstrip(), rstrip(), and strip().
name5 = "\t  Rasel Ahmed \n"
print(name5)
print(name5.lstrip())
print(name5.rstrip())
print(name5.strip())

# 2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename. Then use the removesuffix(0 method to display the filename without the file extension, like some file browsers do.
filename = "python_notes.txt"
print(filename.removesuffix('.txt'))

# 2-9. Number Eight: Write addition, subtraction, multiplication, and division operations that each result in the number 8. Be sure to enclose your operations in print() calls to see the results. You should create four lines that look like this: print(5+3). Your output should be four lines with the number 8 appearing once on each line.
print(5+3)
print(13-5)
print(2*4)
print(int(72/9))

# 2-10. Favorite Number: Use a variable to represent your favorite number. Then, using that variable, create a message that reveals your favorite number. Print that message.
favorite_number = 7
print(f"My favorite number is {favorite_number}.")

# 2-11. Adding Comments: Choose two of the programs you wrote in this chapter, and add at least one comment to each. If you don't have anything specific to write because your programs are too simple at this point, just add your name and the date at the top of each program file. Then write one sentence describing what the program does.
# This program will print my name:
print("Rasel Ahmed")
# This program will print current date/time:
import time
print(f"{time.ctime()}\n")

# 2-12. Zen of Python: Enter import this into a Python terminal session and skim through the additional principles.
import this



