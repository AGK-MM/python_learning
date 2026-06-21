# Strings
# Single or double quotes can be used to create strings in Python.
# Example:
x = "Hello, World!"
y = "Hello, World!"
print(x)
print(y)
# Triple quotes can be used to create a multiline string.
# Example:
z = """AI is transforming our world.
It helps software engineers write better code faster.
Learning python is the best way to start building AI application!"""
# String Length
name = "Aung"
print(len(name))
# String Indexing
print(name[0])
print(name[-1])
# String Slicing
name = "AungKhantZaw"
print(name[:])  # Start to End
print(name[0:])  # Slice to the end
print(name[:5])  # Slice from the start
# Escape Sequence
print("Hello\nWorld")
print("Hello\tWorld")
print("He said 'Hello'")
# Concatenate String
x = "Aung"
y = "Khant"
print(x + y)
print(x + " " + y)
# Formatted String or f-string
age = 26
print(f"My name is {x}{y} and I am {age} years old.")
# String methods
x = " pyhton coding "
print(x.upper())
print(x.lower())
print(x.strip())
print(x.replace("coding", "programming"))
