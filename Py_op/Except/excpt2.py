# Python provides two very important features to handle any unexpected
# error in your Python programs and to add debugging capabilities in them −
#
# Exception Handling − This would be covered in this tutorial.
#
# Assertions − This would be covered in Assertions in Python tutorial.

# Here is a list standard Exceptions available in Python: Standard Exceptions.:
# Exception
# AssertionError
# AttributeError
# EOFError
#
# IndexError
# KeyError
# NameError
# ValueError
# TypeError
#
# IOError
# OSError
# RuntimeError

try:
   # You do your operations here;
   # ......................
except ExceptionI:
   # If there is ExceptionI, then execute this block.
except ExceptionII:
   # If there is ExceptionII, then execute this block.
   # ......................
else:
   # If there is no exception then execute this block.

# A single try statement can have multiple except statements. This is useful
# when the try block contains statements that may throw different types of exceptions.
#
# You can also provide a generic except clause, which handles any exception.
#
# After the except clause(s), you can include an else -clause. The code in the else -block executes if the code in the
# try: block does not raise an exception.
# The else -block is a good place for code that does not need the try: block's protection