# The most essential benefit is to inform the user of the error, while still allowing the program to proceed.

# The rule of thumb is you should raise an exception when your code will possibly
# run into some scenarios when execution can’t proceed. By raising a proper exception,
# it will allow other parts of your code to handle the exception properly, such that the execution can proceed.

def try_syntax(numerator, denominator):
    try:
        print(f'In the try block: {numerator}/{denominator}')
        result = numerator / denominator
    except ZeroDivisionError as zde:
        print(zde)
    else:
        print('The result is:', result)
        return result
    finally:
        print('Exiting')

# try_syntax(12, 4)
# print(try_syntax(11, 0))


# 1. Variable assignment
# except TypeError as e


# 2. Multiple exceptions
# We’ll simply wrap possible exceptions in a tuple

# except (ValueError, ZeroDivisionError) as e:
# print(f"Error {type(e)}: {e}")

def divide_six(number):
    try:
        num = int(number)
        res = 6/num
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error {type(e)}: {e}")

divide_six("six")
# Error <class 'ValueError'>: invalid literal for int() with base 10: 'six'
divide_six(0)
# Error <class 'ZeroDivisionError'>: division by zero

# 3. Multiple except clauses

# 4.
# Another important thing to note with the use of the finally clause
# is that if the try clause includes a break, continue, and return statement,
# the finally clause will run first before executing the break, continue,
# or return statement. Many people can make mistakes here. Let’s take a look at a trivial example below:

 # Check the order of running
def get_integer(number):
    try:
        return int(number)
    except:
        print("Error Encountered")
    finally:
        return "No Numbers!"
 
 # Use the function
get_integer(5)
# 'No Numbers!'
get_integer("hello")
# Error Encountered
# 'No Numbers!'

# Exception with a custom message
# The way you raise your own exceptions is with the raise statement.
# raise ValueError("You can't divide something with zero.")


# it’s possible that we can re - raise the exception and pass the exception to the
# outside scope to see if it can be handled.Such passing of the exception to
# the outside is also known as bubbling up or propagation.


##
# In the below code, we first define a function, read_data, that can read a file.
# Suppose that the other function process_data is a public API and we don’t have good control
# over what file type the user is going to pass. Therefore, when we read the data using the read_data function,
# we want to raise an exception, because our program can’t proceed without the correct data.
# We call the public API process_data function twice, with one using the wrong data type and the other
# using the correct data type. For the former condition, the exception is properly raised and handled
# such that our program doesn’t crash and the user is also informed of the mistake about the API use.

def read_data(filename):
    filename = filename.split(".")
    if file_parts[-1] != "csv":
        print("Wrong data type")
        raise Exception("Can't read non-csv data.")
    else:
        print("CSV data is read")

# Public API
def process_data(file_name):
    try:
        read_data(filename)
    except Exception as e:
        print(f"error: {type(e)} and {e}")
    else:
        print("Further process the data.")

process_data("test.docx")
# Wrong data type.
# Error: Can't read non-csv data.
process_data("test.csv")
# CSV data is read.
# Further process the data.


##
def fibonacci(N):
    L = []
    a, b = 0, 1
    while len(L) < N:
        a, b = b, a + b
        L.append(a)
    return L
# One potential problem here is that the input value could be negative. This will not currently
# cause any error in our function, but we might want to let the user know that a negative N is not supported.
# Errors stemming from invalid parameter values, by convention, lead to a ValueError being raised:

def fibonacci(N):
    if N < 0:
        raise ValueError("N must be non-negative")
    L = []
    a, b = 0, 1
    while len(L) < N:
        a, b = b, a + b
        L.append(a)
    return L

##
# Now the user knows exactly why the input is invalid, and could even use a try...except block to handle it!

N = -10
try:
    print("trying this...")
    print(fibonacci(N))
except ValueError:
    print("Bad value: need to do something else")
# trying this...
# Bad value: need to do something else

##
# Creating Custom Exception Class

class EmployeeModuleError(Exception):
    """Base Exception Class for our Employee module"""
    pass


class EmployeeNotFoundError(EmployeeModuleError):
    """Error raised when employee is not found in the database"""

    def __init__(self, emp_id, msg):
        self.employee_id = emp_id
        self.error_message = msg


class EmployeeUpdateError(EmployeeModuleError):
    """Error raised when employee update fails"""

    def __init__(self, emp_id, sql_error_code, sql_error_msg):
        self.employee_id = emp_id
        self.error_message = sql_error_msg
        self.error_code = sql_error_code


# Nested try-except Blocks Example
# We can have nested try-except blocks in Python. In this case, if an exception is raised in the nested try block,
# the nested except block is used to handle it. In case the nested except is not able to handle it,
# the outer except blocks are used to handle the exception.

x = 10
y = 0

try:
    print("outer try block")
    try:
        print("nested try block")
        print(x / y)
    except TypeError as te:
        print("nested except block")
        print(te)
except ZeroDivisionError as ze:
    print("outer except block")
    print(ze)

##
# Python Exception Handling Best Practices
# Always try to handle the exception in the code to avoid abnormal termination of the program.

# When creating a custom exception class, suffix its name with “Error”.

# If the except clauses have the same code, try to catch multiple exceptions in a single except block.

# Use finally block to close heavy resources and remove heavy objects.

# Use else block to log successful execution of the code, send notifications, etc.

# Avoid bare except clause as much as possible. If you don’t know about the exceptions, then only use it.

# Create module-specific exception classes for specific scenarios.

# You can catch exceptions in an except block and then raise another exception that is more meaningful.

# Always raise exceptions with meaningful messages.

# Avoid nested try-except blocks because it reduces the readability of the code.


