"""
pass statement is a null statement which can be used as a placeholder for future code.

Suppose we have a loop or a function that is not implemented yet, but we want to implement it in the future. In such cases, we can use the pass statement.
"""


n = 10

# use pass inside if statement
if n > 10:
    pass

print('Hello')


"""
Here, notice that we have used the pass statement inside the if statement .

However, nothing happens when the pass is executed. It results in no operation (NOP).
"""