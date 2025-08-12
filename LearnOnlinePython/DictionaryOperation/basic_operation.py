# Basic Dictionary Operations
person = {
    'name': 'alice',
    'age': 25,
    'city': 'new york'
}

print(f"Person Information: {person}")
print()
print(f"Name: {person['name'].capitalize()}")
print(f"Age: {person['age']}")

print()
# Check if a key exists
inventory = {
    'apples': 10,
    'bananas': 5,
    'oranges': 8
}
print(f"Apples in stock: {inventory['apples']}")

if 'grapes'.lower() in inventory:
    print(f"Avaialbe Grapes in stock: {inventory['grapes']}")
else:
    print(f"Grapes are not available in stock.")

print()

# Configuaration Settings
config = {
    'database_url': 'localhost:5432',
    'debug_mode': True,
    'max_connections': 100,
    'timeout': 30
}
print(f"Debug Mode: {config['debug_mode']}")
print(f"Max conections: {config['max_connections']}")
print()

# Data Mapping
grade_points = {
    'A': 4.0,
    'B': 3.0,
    'C': 2.0,
    'D': 1.0,
    'F': 0.0
}
student_grade = 'A'
gpa_value = grade_points[student_grade]
print(f"Grade {student_grade} = {gpa_value} points")
print()

# counting and Frequency
text = "python is great and python is easy to learn"
word_count = {}

for word in text.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(f"Word frequencies: {word_count}")
print()

