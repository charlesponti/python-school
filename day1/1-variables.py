"""
Lesson for learning variables in Python.
"""

# Declare a variable and initialize it
customer_name = "Charles Ponti"
print(customer_name)

# re-declaring the variable works
# customer_name = "Shana Burgos"
# print(customer_name)

# ERROR: variables of different types cannot be combined
# print("this is a string" + 123) # 🤔
# print("this is a string" + "123")

# Global vs. local variables in functions
# def some_function():
#     global customer_name
#     customer_name = "Lucy Uren"
#     print(customer_name)
# some_function()
# print(customer_name)

# Delete variable from namespace 💣
# del customer_name
# print(customer_name)
