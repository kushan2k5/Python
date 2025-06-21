# -----------------------------------------------------------
# Basic Python Function and Conditional Demo
#
# This script demonstrates how to define a simple function in Python
# and use its result in a conditional expression. It’s useful for
# understanding basic function syntax and decision-making with if-else.
# -----------------------------------------------------------

# import panda
# print(dir(pandas))
def add(a,b):
    s= a+b
    return s
print(add(10,15))
if(add(2,5)%2==0):
    print('even')
else:
    print('odd')
# -----------------------------------------------------------
# Conclusion:
# We created an `add` function and used its result to determine
# if the sum is even or odd. This script illustrates foundational
# Python skills that are important for any beginner.
# -----------------------------------------------------------